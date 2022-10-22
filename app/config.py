from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    # proxy settings
    root_path: str = ""

    class Config:
        env_file = ".env"
