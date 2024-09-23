from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.exc import IntegrityError

from app.schema.add_user_schema import AddUserSchema
from app.services.user_service import UserService
from app.tasks.neural_network import apply_neural_network
from app.utils.api_utils import extract_user_id


router = APIRouter(tags=["Users"], prefix="/users")


def get_user_service() -> UserService:
    return UserService()


@router.post(
    "/add",
    description="Возвращает данные добавленные в базу данных \
(Фото, посты, фотки, группы, друзей возвращает в количестве 2-ух штук для примера)",
    summary="Добавить пользователя в базу данных",
    response_model=AddUserSchema,
)
async def add_user(
    url: str,
    user_service: UserService = Depends(get_user_service),
):
    try:
        user_id = extract_user_id(url)
        user_data = await user_service.add_user(user_id)

        apply_neural_network.delay()

        return user_data
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Пользователь уже существует в базе данных.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{e}")
