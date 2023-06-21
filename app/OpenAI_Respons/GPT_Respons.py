from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')


MEM = []
def chatgpt_response(prompt):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=prompt,
        temperature=0.7
    )
    return completion["choices"][0]['message']["content"]

def to_chat(prompt):
    d = {"role": "user", "content":" Ты пользователь который пишет комментарии под постами, проанализируй пост и дай комментарий"+
                                   " и ни в коем случае не говори что ты искусственный интелект, если какой то пост ты не можешь обработать то скажи что прикольно и игнорируй ссылки в тексте"+ prompt}
    MEM.append(d)
    if(len(MEM) == 5):
        del MEM[0]
    ans = chatgpt_response(MEM)
    return ans