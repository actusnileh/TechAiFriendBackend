from typing import AsyncIterator
from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import routers as v1_routers
from app.core.configs import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    await settings.initiate_database()
    yield


def create_app():
    app = FastAPI(
        debug=settings.DEBUG,
        lifespan=lifespan,
        title=settings.SERVICE_NAME,
        version="0.0.1",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(v1_routers, prefix="/v1")

    return app
