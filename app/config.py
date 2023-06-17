from pydantic import BaseSettings


class Settings(BaseSettings):
    open_weather_map_api_key: str = "hello"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
