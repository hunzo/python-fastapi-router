from fastapi import APIRouter
from fastapi.params import Body
from models import Auth

route = APIRouter()


@route.get("/")
async def unprotect():
    return {
        "status": "unprotect"
    }


@route.post("/authentication")
async def authentication(req: Auth.Users = Body(...)):
    return {
        "username": req.username,
        "password": req.password
    }
