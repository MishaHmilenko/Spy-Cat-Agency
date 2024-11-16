from contextlib import asynccontextmanager

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from src.api.controllers.main import setup_controllers
from src.db.main import DBConfig
from src.dishka.container import container


def build_app() -> FastAPI:
    app = FastAPI(title='Spy Cat Agency')

    setup_controllers(app)
    setup_dishka(container, app)

    return app
