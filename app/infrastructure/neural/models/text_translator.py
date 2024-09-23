from transformers import MarianMTModel, MarianTokenizer
import torch


class TextTranslator:
    def __init__(self, batch_size=1):
        self.batch_size = batch_size
        model_name = "Helsinki-NLP/opus-mt-en-ru"
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

        self.device = "cpu"
        self.model.to(self.device)

    def processing(self, texts):
        translations = []
        for i in range(0, len(texts), self.batch_size):
            batch_texts = texts[i: i + self.batch_size]
            answers = self.get_translation(batch_texts)
            translations.extend(answers)
        return translations

    def get_translation(self, texts):
        inputs = self.tokenizer(
            texts, return_tensors="pt", padding=True, truncation=True
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(**inputs)

        batch_translations = self.tokenizer.batch_decode(
            outputs, skip_special_tokens=True
        )

        return batch_translations
