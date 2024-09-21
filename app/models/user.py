from sqlalchemy import (
    Column,
    Float,
    Integer,
    String,
)

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vk_id = Column(Integer, nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    date_of_birth = Column(String, nullable=False)
    year_of_birth = Column(Integer, nullable=True)
    average_likes_photos = Column(Float, nullable=False)
    average_likes_posts = Column(Float, nullable=False)
    interest = Column(String, nullable=True)
    friends_count = Column(Integer, nullable=False)
    posts_count = Column(String, nullable=False)
    photo_count = Column(String, nullable=False)
