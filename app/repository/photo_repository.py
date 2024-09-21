from app.models.photo import Photo
from app.repository.base_repository import BaseRepository


class PhotosRepository(BaseRepository):
    model = Photo
