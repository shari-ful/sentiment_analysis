from fastapi import FastAPI
from . import routs

app = FastAPI()

app.include_router(routs.api)