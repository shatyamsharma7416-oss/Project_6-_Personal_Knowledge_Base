from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/",
    api_key=os.getenv("GOOGLE_AI_STUDIO")
)


response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages= [
        {"role":"user", "content":"What is nation anthem of India and why?"}
    ],
    stream=True
)

print("\033[92mBot:\033[0m ", end="", flush=True)  # green "Bot:" label
for reply_chunk in response:
    piece = reply_chunk.choices[0].delta.content
    print(piece, end="", flush=True)

