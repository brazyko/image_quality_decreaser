import uuid
from fastapi import File, UploadFile, APIRouter
from src.services.images import ImageProcessor
from src.tasks.images import resize_image

router = APIRouter(prefix="/images_processor")


@router.post("/upload/", status_code=200)
async def upload_file(file: UploadFile = File(...)) -> dict:
    image_processor = ImageProcessor()
    image_id = await image_processor.image_uploader(file=file)
    # send task to celery
    task_id = uuid.uuid4().hex
    resize_image.apply_async(
        task_id=task_id,
        kwargs={"image_id": image_id},
    )
    return {"task_id": task_id, "image_id": image_id}


@router.get("/result/", status_code=200)
async def get_result(image_id: str, quality: int):
    image_processor = ImageProcessor()
    result_path = await image_processor.get_image_resized(image_id=image_id, quality=quality)
    result_link = await image_processor.upload_file(image_path=result_path)
    return result_link
