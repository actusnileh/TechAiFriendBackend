from app.core.configs.database import MongoSettings
from app.core.configs.general import GeneralSettings


class Settings(MongoSettings, GeneralSettings):
    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
