class ClothesStyle:
    def __init__(self, processor):
        self.processor = processor

        self.clothing_styles = [
            "Casual",
            "Formal",
            "Sporty",
            "Punk",
            "Goth",
            "Vintage",
            "Bohemian",
            "Preppy",
            "Hip-hop",
            "Streetwear",
            "Chic",
            "Grunge",
        ]

        self.styles_question = (
            "What clothes style?  " + " or ".join(self.clothing_styles) + "?"
        )

    def processing(self, images):
        return [
            self.detect_style(styles)
            for styles in self.processor.get_answer(
                images,
                [self.styles_question for _ in images],
                k=5,
            )
        ]

    def detect_style(self, styles):
        for style in styles:
            for base_category in self.clothing_styles:
                if base_category.lower() in style.lower():
                    return base_category
        return self.clothing_styles[0]
