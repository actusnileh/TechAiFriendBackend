from app.repository.user_repository import UserRepository
from app.schema.user_schema import AddUserSchema


class UserService:
    def __init__(self, user_repository: type[UserRepository]):
        self.user_repository = user_repository

    async def add_user(self, user: AddUserSchema):
        user_data = user.model_dump()
        await self.user_repository.add(**user_data)
