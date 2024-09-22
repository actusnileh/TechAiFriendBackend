from sqlalchemy import select

from app.core.database import async_session_maker
from app.models.photos import Photos
from app.repository.base_repository import BaseRepository


class PhotosRepository(BaseRepository):
    model = Photos

    @classmethod
    async def get_all_photo_urls(cls):
        async with async_session_maker() as session:
            query = select(cls.model.photo_url)
            result = await session.execute(query)
            return result.scalars().all()
