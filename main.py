from fastapi import FastAPI

from infra.routes.users.create_teacher import router as create_teacher_router

app = FastAPI()

app.include_router(create_teacher_router)

from infra.routes.users.create_student import router as create_student_router
app = FastAPI()

app.include_router(create_student_router)


