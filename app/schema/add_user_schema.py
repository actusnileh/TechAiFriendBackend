from typing import (
    List,
    Optional,
)

from pydantic import BaseModel


class PostSchema(BaseModel):
    vk_id: int
    date: str
    text: str
    author: str
    friend_or_not_friend: bool


class PhotoSchema(BaseModel):
    photo_id: int
    url: str
    likes_count: int
    description: Optional[str]


class GroupSchema(BaseModel):
    id: int
    name: str
    description: Optional[str]


class FriendSchema(BaseModel):
    id: int
    city: str
    education: Optional[str]
    job: Optional[str]


class UserSchema(BaseModel):
    vk_id: int
    age: int
    date_of_birth: Optional[str]
    year_of_birth: Optional[int]
    average_likes_photos: float
    average_likes_posts: float
    interest: str
    friends_count: int
    posts_count: str
    photo_count: str
    posts: List[PostSchema]
    photos: List[PhotoSchema]
    groups: List[GroupSchema]
    friends: List[FriendSchema]


class AddUserSchema(BaseModel):
    message: str
    data: Optional[UserSchema]
