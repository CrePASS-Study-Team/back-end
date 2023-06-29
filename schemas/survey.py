from pydantic import BaseModel


class mbti_answer(BaseModel):
    a : str
    b : str
    c : str
    d : str
    e : str


class mbti_question(BaseModel):
    id : str
    question : str
    answers : mbti_answer


class user_answer(BaseModel):
    id : str
    answer : str


class user_select(BaseModel):
    questions: list[mbti_question]
    answers : list[user_answer] 


class result_mbti(BaseModel):
    result : str
