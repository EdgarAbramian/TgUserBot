from dotenv import load_dotenv
import os
from pyrogram import Client, filters
from app.OpenAI_Respons.GPT_Respons import to_chat
from pyrogram.types.messages_and_media.message import Message
import pyrogram
load_dotenv()
API_ID = os.getenv('api_id')
API_HASH = os.getenv('api_hash')


app = Client("my_account", API_ID, API_HASH, device_model="Comment On Channel",
    app_version="CoCh v1.0",)

@app.on_message(filters.channel)
def comment_sender(client:Client, message:Message):
    post = client.get_discussion_message(message.chat.id, message.id)
    post.reply(to_chat(message.text))


























