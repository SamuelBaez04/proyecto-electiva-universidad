from fastapi import APIRouter, Depends, HTTPException, Request, Body
from domain.dtos.teacher_dto import TeacherDTO

router = APIRouter()

@router.post("/user/teacher")
async def create_teacher(request: Request, teacher: TeacherDTO = Body()):
    pass