import torch
from transformers import (
    ViltForQuestionAnswering,
    ViltProcessor,
)


class ImageQuestions:
    def __init__(self, batch_size=1):
        self.batch_size = batch_size
        self.processor = ViltProcessor.from_pretrained(
            "dandelin/vilt-b32-finetuned-vqa",
        )
        self.model = ViltForQuestionAnswering.from_pretrained(
            "dandelin/vilt-b32-finetuned-vqa",
        )

        self.device = "cpu"

        self.model.to(self.device)

    def get_answer(self, images, questions, k=5):
        encoding = self.processor(
            images=images,
            text=questions,
            return_tensors="pt",
            padding=True,
        ).to(self.device)
        with torch.no_grad():
            outputs = self.model(**encoding)
        logits = outputs.logits
        idxs = [torch.topk(logit, k, dim=-1).indices.tolist() for logit in logits]
        answers = [[self.model.config.id2label[x] for x in idx] for idx in idxs]
        return answers
