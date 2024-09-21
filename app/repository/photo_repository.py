from app.models.photos import Photos
from app.repository.base_repository import BaseRepository


class PhotosRepository(BaseRepository):
    model = Photos
