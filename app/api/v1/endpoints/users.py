from fastapi import (
    APIRouter,
    Depends,
)

from app.services.user_service import UserService
from app.utils.api_utils import extract_user_id


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
    try:
        user_id = extract_user_id(url)
        await user_service.add_user(user_id)
    except Exception as e:
        return {"error": str(e)}
    else:
        return {"message": "User added successfully"}
