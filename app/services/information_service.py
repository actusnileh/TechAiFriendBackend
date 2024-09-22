import csv
import io

from fastapi import HTTPException
from fastapi.responses import StreamingResponse

from app.repository.friends_repository import FriendsRepository
from app.repository.groups_repository import GroupsRepository
from app.repository.photo_repository import PhotosRepository
from app.repository.posts_repository import PostsRepository
from app.repository.user_repository import UserRepository


def model_to_dict(model):
    return {
        column.name: getattr(model, column.name) for column in model.__table__.columns
    }


TABLES_MODELS = {
    "users": UserRepository,
    "posts": PostsRepository,
    "photos": PhotosRepository,
    "groups": GroupsRepository,
    "friends": FriendsRepository,
}


class InformationService:

    @staticmethod
    async def get_all_information(table_name):
        repo = TABLES_MODELS.get(table_name)

        if not repo:
            raise HTTPException(status_code=404, detail="Table not found")

        data = await repo().find_all()

        output = io.StringIO()
        writer = csv.writer(output)

        if data:
            writer.writerow(model_to_dict(data[0]).keys())
            for row in data:
                writer.writerow(model_to_dict(row).values())

        output.seek(0)

        return StreamingResponse(
            output,
            media_type="text/csv",
            headers={"Content-Disposition": f"attachment; filename={table_name}.csv"},
        )
