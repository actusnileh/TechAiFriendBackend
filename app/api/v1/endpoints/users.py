from fastapi import (
    APIRouter,
    Depends,
)

from app.services.user_service import UserService


router = APIRouter(tags=["Users"], prefix="/users")


def get_user_service() -> UserService:
    return UserService()


@router.post(
    "/add",
    summary="Добавить пользователя в базу данных",
)
async def add_user(
    url: str,
    user_service: UserService = Depends(get_user_service),
):
    await user_service.add_user(url)
    return {"message": "User added successfully"}
