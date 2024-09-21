from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import relationship
from app.core.database import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)

    post_vk_id = Column(Integer, nullable=False)
    post_date = Column(String, nullable=False)
    post_text = Column(String, nullable=True)
    post_author = Column(Integer, nullable=False)
    post_friend_or_not_friend = Column(Boolean, nullable=False)

    user = relationship("User", back_populates="posts")
