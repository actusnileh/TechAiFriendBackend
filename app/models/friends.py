from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from app.core.database import Base


class Friends(Base):
    __tablename__ = "friends"

    id = Column(Integer, primary_key=True, autoincrement=True)

    friend_id = Column(Integer, nullable=False)
    friend_city = Column(String, nullable=True)
    friend_education = Column(String, nullable=True)
    friend_job = Column(String, nullable=True)

    user = relationship("User", back_populates="friends")
