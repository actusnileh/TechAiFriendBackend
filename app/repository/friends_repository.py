from app.models.friends import Friends
from app.repository.base_repository import BaseRepository


class FriendsRepository(BaseRepository):
    model = Friends
