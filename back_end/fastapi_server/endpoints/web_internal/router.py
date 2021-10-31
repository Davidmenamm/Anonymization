from fastapi import APIRouter

router = APIRouter(
			prefix="/web_internal",
    		tags=["web_internal"],
			responses={404: {"description": "Not found"}}
			)


@router.get("/")
async def web_internal():
    pass