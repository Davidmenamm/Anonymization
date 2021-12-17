''' web directory router file'''
''' imports '''
from fastapi import APIRouter

''' router '''
router = APIRouter(
			prefix="/web_external",
    		tags=["web_external"],
			responses={404: {"description": "Not found"}}
			)

''' default endpoint '''
@router.get("/")
async def dafault_endpoint():
    return { 'message': 'Currently, no endpoints are present for this path!'}




	