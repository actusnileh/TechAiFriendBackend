class ImageCategory:
    def __init__(self, processor):
        self.processor = processor

        self.categories = ["man", "women", "collective", "landscape", "other"]

        self.categories_question = (
            "what is the category of this photo? " + " or ".join(self.categories) + "?"
        )

    def processing(self, images):
        return [
            self.detect_category(categories)
            for categories in self.processor.get_answer(
                images, [self.categories_question for _ in images], k=3
            )
        ]

    def detect_category(self, categories):
        for category in categories:
            for base_category in self.categories:
                if base_category in category:
                    return base_category
        return self.categories[-1]
