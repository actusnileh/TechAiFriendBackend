from enum import Enum

from pydantic import BaseModel


class TableNameEnum(str, Enum):
    users = "users"
    posts = "posts"
    photos = "photos"
    groups = "groups"
    friends = "friends"


class TableRequest(BaseModel):
    table_name: TableNameEnum
