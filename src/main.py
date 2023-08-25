from typing import Callable

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from src.api.routers import images_router
from src.config.settings import settings


def init_app() -> FastAPI:
    application = FastAPI(
        title=f"{settings.PROJECT_NAME}🚀🚀🚀",
        description=f"API docs for {settings.PROJECT_NAME}",
        version="0.0.1",
        contact={
            "name": "Bohdan Odintsov",
            "email": "odintsov.bohdan@gmail.com",
        },
    )

    register_middleware(application)
    application.include_router(images_router)
    application.add_event_handler("shutdown", on_shutdown_handler(application))
    logger.info("App running ...")
    return application


def on_shutdown_handler(application: FastAPI) -> Callable:  # type: ignore
    async def stop_app() -> None:
        pass
        # TODO call required functions on stop_app

    return stop_app


def register_middleware(application: FastAPI) -> None:
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(item) for item in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


app = init_app()
