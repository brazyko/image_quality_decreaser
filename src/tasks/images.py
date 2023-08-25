import os
from typing import Optional

from PIL import Image

from src.config.celery_app import celery_app
from src.config.settings import SettingsBase


@celery_app.task()
def resize_image(image_id: Optional[str]) -> None:
    image_path = os.path.join(
        SettingsBase.UPLOADS_DIR, f"{image_id}.png"
    )  # Images are stored as PNG
    for quality in SettingsBase.QUALITY_LIST:
        image = Image.open(os.path.join(image_path))
        width, height = image.size
        new_width = int(width * quality / 100)
        new_height = int(height * quality / 100)
        scaled_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        # Convert RGBA image to RGB before saving as JPEG
        rgb_scaled_image = scaled_image.convert("RGB")

        result_path = os.path.join(SettingsBase.RESULTS_DIR, f"{image_id}_{quality}.jpg")
        rgb_scaled_image.save(result_path, "JPEG")
