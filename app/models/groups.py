from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from app.core.database import Base


class Groups(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, autoincrement=True)

    group_id = Column(Integer, nullable=False)
    group_name = Column(String, nullable=False)
    group_description = Column(String, nullable=True)

    user = relationship("User", back_populates="groups")
