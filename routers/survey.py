from fastapi import APIRouter, Response, status, HTTPException
from services.survey import create_MBTI_questions, get_MBTI_results
from schemas.survey import mbti_question, user_select, result_mbti


router = APIRouter(tags=["survey"])


@router.post("/questions", response_model=list[mbti_question])
def survey_get_questions(response:Response):
    response_data = create_MBTI_questions()

    if response_data is False:
        raise HTTPException(
                status_code=202,
                detail="The request was accepted for processing, but processing was not completed. Please try again.",
                )

    response.status_code = status.HTTP_200_OK
    return response_data


@router.post("/answers", response_model=result_mbti)
def survey_get_anwsers(item:user_select, response:Response):
    data = item.dict()
    response_data = get_MBTI_results(data)

    if response_data is False:
        raise HTTPException(
                status_code=202,
                detail="The request was accepted for processing, but processing was not completed. Please try again.",
                )

    response.status_code = status.HTTP_200_OK
    return response_data
