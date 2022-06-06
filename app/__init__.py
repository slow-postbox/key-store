from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI(
    title="Key Store",
    version="1.0.0"
)

versions = [
    "v1",
]

for version in [__import__(x) for x in versions]:
    dummy = APIRouter(
        prefix="/" + version.__name__,
        tags=[version.__name__]
    )

    for route in getattr(version, "__all__"):
        dummy.include_router(getattr(getattr(version, route), "router"))

    app.include_router(dummy)
