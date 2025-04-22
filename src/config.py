from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    HOST: str
    PORT: int

    LOGFIRE_TOKEN: str

    RETOOL_WORKFLOW_URL: str
    RETOOL_WORKFLOW_API_KEY: str

    DATABASE_URL: str

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )


config: Config = Config()
