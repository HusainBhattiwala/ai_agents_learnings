from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(prefix="/healthcheck")


class HealthcheckResponse(BaseModel):
    status: str


@router.get("/")
def healthcheck(
    request: Request ,
):
    return HealthcheckResponse(status="ok")
