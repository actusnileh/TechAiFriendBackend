from PIL import Image
import requests
from app.infrastructure.neural.models.image_desc import ImageDesc
from app.infrastructure.neural.models.image_questions import ImageQuestions
from app.infrastructure.neural.models.text_translator import TextTranslator
from app.infrastructure.neural.processors.clothes_color import ClothesColor
from app.infrastructure.neural.processors.clothes_style import ClothesStyle
from app.infrastructure.neural.processors.image_category import ImageCategory
from app.repository.photo_repository import PhotosRepository
from app.core.database import async_session_maker


class NeuralNetworkProcessor:
    def __init__(self, batch_size: int = 20):
        self.batch_size = batch_size

    async def load_images(self, batch_images):
        return [
            Image.open(requests.get(batch_image, stream=True).raw).convert("RGB")
            for batch_image in batch_images
        ]

    async def process_batch(self, batch_photos):
        batch_images = [photo.photo_url for photo in batch_photos]
        result = {"image_url": batch_images}

        # Загружаем изображения
        batch_images = await self.load_images(batch_images)

        # Описание изображений
        image_desc = ImageDesc(batch_size=self.batch_size)
        result["descriptions"] = image_desc.processing(batch_images)

        # Перевод описаний
        text_transc = TextTranslator(batch_size=self.batch_size)
        result["descriptions_russian"] = text_transc.processing(result["descriptions"])

        # Вопросы по изображению и их анализ
        image_que = ImageQuestions(batch_size=self.batch_size)

        # Анализ цветов одежды
        image_colors = ClothesColor(image_que)
        result["colors"] = image_colors.processing(batch_images)

        # Определение категорий
        image_category = ImageCategory(image_que)
        result["categories"] = image_category.processing(batch_images)

        # Определение стилей одежды
        c_color = ClothesStyle(image_que)
        result["styles"] = c_color.processing(batch_images)

        return result

    async def update_photos(self, batch_photos, result):
        async with async_session_maker() as session:
            for i, photo in enumerate(batch_photos):
                photo.photo_description = result["descriptions"][i]
                photo.photo_description_ru = result["descriptions_russian"][i]
                photo.photo_description_colors = (
                    result["colors"][i]
                    if result["colors"][i] is not None
                    else "Multicolored"
                )
                photo.photo_description_category = result["categories"][i]
                photo.photo_description_style = result["styles"][i]
                session.add(photo)
            await session.commit()

    async def run(self):
        batch_photos = await PhotosRepository.get_photo_without_description()
        if not batch_photos:
            return
        result = await self.process_batch(batch_photos)
        print(result)
        await self.update_photos(batch_photos, result)
