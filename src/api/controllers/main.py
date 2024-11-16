from fastapi import FastAPI

from src.api.controllers.spy_cat import router as spy_cat_router
from src.api.controllers.target import router as target_router
from src.api.controllers.mission import router as mission_router

def setup_controllers(app: FastAPI) -> None:

    app.include_router(router=spy_cat_router)
    app.include_router(router=target_router)
    app.include_router(router=mission_router)