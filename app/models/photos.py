from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.core.database import Base


class Photos(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.vk_id'))

    photo_id = Column(Integer, nullable=False)
    photo_url = Column(String, nullable=False)
    photo_count_likes = Column(Integer, nullable=False)
    photo_description = Column(String, nullable=True)

    user = relationship("User", back_populates="photo")
