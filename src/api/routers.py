from fastapi import APIRouter


from src.api.endpoints.images import router as images_processor


images_router = APIRouter(prefix=f"/images", tags=[f"images"])  # noqa
images_router.include_router(images_processor)
