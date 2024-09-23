from sqlalchemy import (
    or_,
    select,
)

from app.core.database import async_session_maker
from app.models.photos import Photos
from app.repository.base_repository import BaseRepository


class PhotosRepository(BaseRepository):
    model = Photos

    @classmethod
    async def get_photo_without_description(cls):
        async with async_session_maker() as session:
            query = (
                select(cls.model)
                .where(
                    or_(
                        cls.model.photo_description.is_(None),
                        cls.model.photo_description_ru.is_(None),
                        cls.model.photo_description_colors.is_(None),
                        cls.model.photo_description_category.is_(None),
                        cls.model.photo_description_style.is_(None),
                    ),
                )
                .limit(2)
            )
            result = await session.execute(query)
            photos = result.scalars().all()
            return photos
