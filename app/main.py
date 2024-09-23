from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes import routers as v1_routers
from app.core.configs import settings
from app.tasks.neural_network import apply_neural_network


async def lifespan(app: FastAPI):
    apply_neural_network.delay()
    yield


def create_app():
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.SERVICE_NAME,
        lifespan=lifespan,
        version="1.0",
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
