# from langchain_openai import ChatOpenAI
# from pydantic import BaseModel
# from typing import Literal
# from dotenv import load_dotenv

# load_dotenv()

# class Intent(BaseModel):
#     intent : Literal["vision","chat"]


# llm = ChatOpenAI(model="gpt-4o-mini",temperature=0)
# structured_llm = llm.with_structured_output(Intent)

# def get_intent(text):
#     prompt = f"""
#     Classify the user input into:
#     - vision (environment, objects, surroundings)
#     - chat (general conversation)

#     Input: {text}
#     """

#     result = structured_llm.invoke(prompt)

#     return result.intent


# print(get_intent("What is infront of me?"))




from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

task_examples = {
    "navigation_check": [
        "can i walk now",
        "is it safe to move",
        "can i go forward",
        "am i clear to step"
    ],
    "scene_description": [
        "what is in front of me",
        "describe surroundings",
        "what do you see",
        "what's around me"
    ],
    "chat": [
        "tell me a joke",
        "how are you",
        "what is AI"
    ]
}


task_embeddings = {}

for task , example in task_examples.items():
    task_embeddings[task] = model.encode(example)


def detect_task(user_input):
    user_emb = model.encode([user_input])

    best_task = "chat"
    best_score = -1

    for task, embeddings in task_embeddings.items():
        scores = cosine_similarity(user_emb, embeddings)
        score = np.max(scores)

        if score > best_score:
            best_score = score
            best_task = task

    return best_task, best_score

def get_intent(user_input):
    task, score = detect_task(user_input)

    if task in ["navigation_check", "scene_description"]:
        return "vision"
    else:
        return "chat"
    

print(get_intent("is there any obstacle infront of me??"))