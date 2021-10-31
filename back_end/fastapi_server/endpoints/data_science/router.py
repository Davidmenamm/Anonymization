from fastapi import APIRouter
from .anonymization import router as anonymization_router

router = APIRouter(
			prefix="/data_science",
    		tags=["data_science"],
			responses={404: {"description": "Not found"}}
			)
router.include_router(anonymization_router.router)


@router.get("/")
async def data_science():
    pass