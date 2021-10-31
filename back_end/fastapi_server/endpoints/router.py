from fastapi import APIRouter
from .data_science import router as router_data
from .web_external import router as router_web_ext
from .web_internal import router as router_web_int

router = APIRouter(
			prefix="/endpoints",
    		tags=["endpoints"],
			responses={404: {"description": "Not found"}}
			)
router.include_router(router_data.router)
router.include_router(router_web_ext.router)
router.include_router(router_web_int.router)


@router.get("/")
async def endpoints():
    pass