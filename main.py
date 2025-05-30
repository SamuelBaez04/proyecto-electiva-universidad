from fastapi import FastAPI
from infra.routes.users.create_teacher import router as create_teacher_router

app = FastAPI()

app.include_router(create_teacher_router)

