import numpy as np


class ClothesColor:
    def __init__(self, processor):
        self.processor = processor

        self.colors = [
            "black",
            "white",
            "red",
            "blue",
            "green",
            "yellow",
            "purple",
            "pink",
            "gray",
            "orange",
        ]

        self.color_question = "What colors are the clothes on the person?"

    def processing(self, images):
        return self.color_analysis(images)

    def color_analysis(self, images):
        colors = np.array(
            [
                self.detect_colors(" ".join(colors))
                for colors in self.processor.get_answer(
                    images, [self.color_question for _ in images], k=3
                )
            ]
        )
        return np.where(colors is None, "Black", colors)

    def detect_colors(self, text):
        for color in self.colors:
            if color in text.lower():
                return color
        return None
