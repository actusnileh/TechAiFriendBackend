from app.models.groups import Groups
from app.repository.base_repository import BaseRepository


class GroupsRepository(BaseRepository):
    model = Groups
