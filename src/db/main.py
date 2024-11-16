import os
from dataclasses import dataclass


@dataclass
class DBConfig:
    user: str = os.getenv("DB_USER")
    password: str = os.getenv("DB_PASSWORD")
    database: str = os.getenv("DB_NAME")
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

