from transformers import AutoProcessor, AutoModelForCausalLM
import torch


class ImageDesc:

    def __init__(self, batch_size=1):
        self.batch_size = batch_size
        self.processor = AutoProcessor.from_pretrained("microsoft/git-base-coco")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/git-base-coco")

        self.device = "cpu"

        self.model.to(self.device)

    def processing(self, images):
        descriptions = []
        for i in range(0, len(images), self.batch_size):
            batch_images = images[i: i + self.batch_size]
            answers = self.get_desc(batch_images)
            descriptions.extend(answers)
        return descriptions

    def get_desc(self, images):
        inputs = self.processor(images=images, return_tensors="pt").to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(**inputs)
        batch_captions = self.processor.batch_decode(outputs, skip_special_tokens=True)

        return batch_captions
