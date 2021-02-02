from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_DEBUG = True

    DB_DSN: str = 'postgresql://app:app@localhost/app'


settings = Settings()
