from fastapi import APIRouter
from .anonymize import anonymize

router = APIRouter(
			prefix="/anonymization",
    		tags=["anonymization"],
			responses={404: {"description": "Not found"}}
			)


@router.get("/")
async def anonymization():
    return anonymize()