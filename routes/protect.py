from fastapi import APIRouter

route = APIRouter()


@route.get("/")
async def protect():
    return {
        "status": "protect"
    }
