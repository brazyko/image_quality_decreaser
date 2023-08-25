import os
import uuid
from typing import Optional
from src.config.settings import SettingsBase
from fastapi.responses import FileResponse


class ImageProcessor:
    def __init__(self) -> None:
        self.uploads_dir = SettingsBase.UPLOADS_DIR
        self.results_dir = SettingsBase.RESULTS_DIR
        self.quality_list = SettingsBase.UPLOADS_DIR

    async def image_uploader(self, file) -> str:  # type: ignore
        image_id = str(uuid.uuid4())
        image_path = os.path.join(self.uploads_dir, f"{image_id}.png")  # Save as PNG
        with open(image_path, "wb") as image_file:
            image_file.write(file.file.read())
        return image_id

    async def get_image_resized(self, image_id: Optional[str], quality: int) -> str:
        image_path = os.path.join(self.results_dir, f"{image_id}_{quality}.jpg")
        return image_path

    @staticmethod
    async def upload_file(image_path):  # type: ignore
        return FileResponse(image_path, media_type="image/jpeg", filename="decreased.jpg")
