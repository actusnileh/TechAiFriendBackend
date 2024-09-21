from app.models.user import User
from app.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    model = User
