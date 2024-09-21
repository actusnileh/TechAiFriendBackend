from app.models.posts import Posts
from app.repository.base_repository import BaseRepository


class PostsRepository(BaseRepository):
    model = Posts
