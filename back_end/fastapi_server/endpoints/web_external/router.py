from fastapi import APIRouter

router = APIRouter(
			prefix="/web_external",
    		tags=["web_external"],
			responses={404: {"description": "Not found"}}
			)


@router.get("/")
async def web_external():
    pass