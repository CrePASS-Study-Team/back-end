import json
import time

from fastapi import FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware

from routers import survey


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(survey.router, prefix="/survey")


@app.get("/")
def root(response:Response):
    response.status_code = status.HTTP_200_OK
    return {"code":200, "detail":"MBTI Project!"}
