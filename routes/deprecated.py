from fastapi import APIRouter

route = APIRouter()

@route.get("/")
async def deprecated():
    return {
        "status": "deprecated"
    }