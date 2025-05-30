from fastapi import APIRouter, Request, Body
from domain.dtos.student_dto import StudentDTO

router = APIRouter()

@router.put('/user/student')
async def create_student(request: Request, student: StudentDTO = Body()):
    """
    Este metodo genera un student
    :param request:
    :param student:
    :return:
    """
    pass