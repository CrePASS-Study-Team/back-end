import time
import json 
import openai

from config import OPENAI_API_KEY 


openai.api_key = OPENAI_API_KEY


sample_data = {
        "questions":[
            {
                "id": 1,
                "question": "When facing a difficult decision, I tend to?",
                "answers": {
                    "a": "Weigh pros and cons and make a logical choice",
                    "b": "Trust my intuition and go with my gut feeling",
                    "c": "Seek advice and input from others",
                    "d": "Follow my personal values and morals",
                    "e": "Research and gather more information before deciding"
                    }
                },
            {
                "id": 2,
                "question": "In a group setting, I am more likely to?",
                "answers": {
                    "a": "Take charge and lead the group",
                    "b": "Offer ideas and suggestions, but let someone else take charge",
                    "c": "Stay quiet and observe",
                    "d": "Focus on completing my own tasks",
                    "e": "Be more comfortable working alone"
                    }
                }
            ]
        }


def preprocess_response(data:str):
    start = data.find('[')
    end = data.rfind(']')+1
    data = data[start:end]
    try:
        data = data.replace("'", '"')
        data = data.replace('"s',"'s")
        data = data.replace('"m',"'m")
        data = data.replace('"t',"'t")
        data = data.replace('"ll',"'ll")
        data = data.replace('"d ',"'d ")
        data = data.replace('"v',"'v")
        data = data.replace('s" ',"s' ")
        data = data.replace("\\'", "'")

        data = data.replace(",]", "]")

        return json.loads(data)
    except Exception as e:
        print("Fail")
        print("-"*20)
        print(data)
        with open(f"/home/data/fail/{str(time.time())}_fail.txt", 'w') as file:
            file.write(data)
        return False


def create_MBTI_questions():

    messages = [{"role": "system", "content": "You are a MBTI Analyst."},
            {"role": "user", "content": f"Please make 20 questions with 5 options for MBTI analysis. The answer should be in the following data format and should not be used. {sample_data}."}]

    completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
            )

    questions = preprocess_response(completion["choices"][0]["message"]["content"])
    if questions != False:
        with open(f"/home/data/succeed/{str(time.time())}_succeed.json", 'w') as file:
            json.dump(questions, file)
        print("Succeed")

    return questions 


def get_MBTI_results(data):
    questions = [str(d) for d in data["questions"]]
    MBTI_questions = " ".join(questions)

    answers = [str(d) for d in data["answers"]]
    MBTI_answers = " ".join(answers)

    messages = [
            {"role": "system", "content": "You are a MBTI Analyst."},
            {"role": "user", "content": f"Please make 20 questions with 5 options for MBTI analysis."},
            {"role": "system", "content": f"{MBTI_questions}"},
            {"role": "user", "content": f"My answer is {MBTI_answers}"}
            ]

    completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
            )

    MBTI_result = completion["choices"][0]["message"]["content"]

    return {"result":MBTI_result}

