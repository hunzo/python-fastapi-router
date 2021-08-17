from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.params import Security
from fastapi.security import APIKeyHeader
from starlette import status
from routes import unprotect, protect, deprecated

app = FastAPI(title="Router Example")

API_KEY = "123456"
API_KEY_NAME = "x-api-key"

api_key_header_auth = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


def check_token(api_key_header: str = Security(api_key_header_auth)):

    if api_key_header != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid KEY"
        )


app.include_router(
    unprotect.route,
    prefix="/unprotect",
    tags=["Unprotect"],
)

app.include_router(
    protect.route,
    prefix="/protect",
    tags=["Protect"],
    dependencies=[Security(check_token)]
)

app.include_router(
    deprecated.route,
    tags=["old services"],
    prefix="/deprecated",
    deprecated=True
)
