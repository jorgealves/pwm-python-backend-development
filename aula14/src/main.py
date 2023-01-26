from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import root, profiles


api = FastAPI(
    title="Social Network API",
    description="An API that everything is possible"
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


routers = [
    root.router,
    profiles.router,
]

for router in routers:
    api.include_router(router=router)

