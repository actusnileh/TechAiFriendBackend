from enum import Enum

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class GeneralSettings(BaseSettings):
    SERVICE_NAME: str = "TechFriendBackend"
    ENVIROMENT: Environment
    DEBUG: bool
