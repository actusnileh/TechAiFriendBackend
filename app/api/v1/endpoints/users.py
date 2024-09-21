from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from app.repository.user_repository import UserRepository
from app.schema.user_schema import AddUserSchema
from app.services.user_service import UserService


router = APIRouter(tags=["Users"], prefix="/users")


def get_user_service() -> UserService:
    return UserService(UserRepository)


@router.post(
    "/add",
    summary="Добавить пользователя в базу данных",
)
async def add_user(
    user: AddUserSchema,
    user_service: UserService = Depends(get_user_service),
):
    try:
        await user_service.add_user(user)
        return {"message": "User added successfully"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")
