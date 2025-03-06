import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

question = input("User: ")
question2 = "What is the capital of United States?"

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    temperature=0.3,
    top_p=1.0,
    max_tokens=50,
    n=1,
    model=model_name
)

for i in range(len(response.choices)):
    print("AI :",response.choices[i].message.content)

