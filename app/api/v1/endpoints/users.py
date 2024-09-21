import re
from fastapi import (
    APIRouter,
    Depends,
)

from app.services.user_service import UserService


router = APIRouter(tags=["Users"], prefix="/users")


def get_user_service() -> UserService:
    return UserService()


def extract_user_id(url: str) -> str:
    match = re.search(r"vk\.com/(.+)$", url)
    if match:
        return match.group(1)
    raise ValueError("Invalid URL format")


@router.post(
    "/add",
    summary="Добавить пользователя в базу данных",
)
async def add_user(
    url: str,
    user_service: UserService = Depends(get_user_service),
):
    user_id = extract_user_id(url)
    await user_service.add_user(user_id)
    return {"message": "User added successfully"}
