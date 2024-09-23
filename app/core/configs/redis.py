from pydantic import model_validator

from app.core.configs.general import GeneralSettings


class RedisSettings(GeneralSettings):
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_URL: str | None = None

    @model_validator(mode="before")  # noqa
    @classmethod
    def RedisURL(cls, values: dict[str, str]) -> dict[str, str]:
        if values.get("REDIS_URL"):
            return values

        host = values.get("REDIS_HOST")
        port = values.get("REDIS_PORT")

        values["REDIS_URL"] = f"redis://{host}:{port}"

        return values
