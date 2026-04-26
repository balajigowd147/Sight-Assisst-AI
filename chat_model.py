from transformers import pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-base")

def chat_response(text):
    return pipe(text)[0]['generated_text']

# print(chat_response("Hii !! What can i have for the dinner?"))