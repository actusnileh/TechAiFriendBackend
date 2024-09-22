from app.repository.photo_repository import PhotosRepository


class PhotoService:
    def __init__(self):
        self.repo = PhotosRepository()

    async def get_all_photos(self):
        return await self.repo.get_all_photo_urls()
