from app.core.configs.database import PostgresSettings
from app.core.configs.general import GeneralSettings
from app.core.configs.redis import RedisSettings


class Settings(PostgresSettings, RedisSettings, GeneralSettings):
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
