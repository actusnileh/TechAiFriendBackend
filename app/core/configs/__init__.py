from app.core.configs.database import PostgresSettings
from app.core.configs.general import GeneralSettings


class Settings(PostgresSettings, GeneralSettings):
    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
