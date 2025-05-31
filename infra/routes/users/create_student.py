from fastapi import APIRouter, Request, Body
from domain.dtos.student_dto import StudentDTO

router = APIRouter()

@router.put('/user/student')
async def create_student(request: Request, student: StudentDTO = Body()):
    """
    this def generate a student from
    :param request:
    :param student:
    :return:
    """
    pass