from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']


client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens=50,
    n=1,
    temperature=1,
    messages=[
        {"role": "user", "content": "hello"},
    ],
)

print(response)