''' data_science router file'''
''' imports '''
from fastapi import APIRouter
from .anonymization import router as anonymization_router

''' router '''
router = APIRouter(
			prefix="/data_science",
    		tags=["data_science"],
			responses={404: {"description": "Not found"}}
			)
router.include_router(anonymization_router.router)

''' default endpoint '''
@router.get("/")
async def dafault_endpoint():
    return { 'message': 'Currently, no endpoints are present for this path!'}