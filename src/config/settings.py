import os
from typing import List

from environs import Env
from pydantic import AnyHttpUrl

env = Env()


class SettingsBase:
    ROOT_DIR = os.path.abspath(os.path.dirname("src"))
    RESULTS_DIR = f"{ROOT_DIR}/src/results"
    UPLOADS_DIR = f"{ROOT_DIR}/src/uploads"
    QUALITY_LIST = [100, 75, 50, 25]

    # Base settings
    # --------------------------------------------------------------------------
    PROJECT_NAME: str = "Image Decrease Resolution"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = env.list(
        "BACKEND_CORS_ORIGINS", ["http://127.0.0.1:8000/"]
    )


def _get_settings():  # type: ignore
    return SettingsBase()


settings = _get_settings()
