''' base router file'''
''' imports '''
from fastapi import APIRouter
from .data_science import router as router_data
from .web import router as router_web

''' router '''
router = APIRouter(
			prefix="/endpoints",
    		tags=["endpoints"],
			responses={404: {"description": "Not found"}}
			)
router.include_router(router_data.router)
router.include_router(router_web.router)

''' default endpoint '''
@router.get("/")
async def dafault_endpoint():
    return { 'message': 'Currently, no endpoints are present for this path!'}