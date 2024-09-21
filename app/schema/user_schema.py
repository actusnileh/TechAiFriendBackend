from pydantic import BaseModel, Field
from typing import Optional


class AddUserSchema(BaseModel):
    vk_id: int = Field(..., description="ID пользователя в VK")
    age: int = Field(..., ge=0, description="Возраст пользователя")
    date_of_birth: str = Field(
        ..., description="Дата рождения пользователя (формат MM-DD)"
    )
    year_of_birth: int = Field(
        ..., ge=1900, le=2025, description="Год рождения пользователя"
    )
    average_likes_photos: float = Field(
        ..., ge=0, description="Среднее количество лайков на фото"
    )
    average_likes_posts: float = Field(
        ..., ge=0, description="Среднее количество лайков на посты"
    )
    interest: Optional[str] = Field(None, description="Интересы пользователя")
    friends_count: int = Field(..., ge=0, description="Количество друзей пользователя")
    posts_count: int = Field(..., ge=0, description="Количество постов пользователя")
    photo_count: int = Field(
        ..., ge=0, description="Количество фотографий пользователя"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "vk_id": 123456789,
                "age": 25,
                "date_of_birth": "05-16",
                "year_of_birth": 1998,
                "average_likes_photos": 24.5,
                "average_likes_posts": 15.7,
                "interest": "Музыка",
                "friends_count": 150,
                "posts_count": 50,
                "photo_count": 200,
            }
        }
