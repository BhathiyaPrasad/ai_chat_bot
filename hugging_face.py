from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ["HUGGINGFACE_TOKEN"]

client = InferenceClient(
	provider="together",
	api_key=token
)

messages = [
	{
		"role": "system",
		"content": "What is the capital of Sri Lanka?"
	}
]

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
	messages=messages,
	max_tokens=500,
)

print(completion.choices[0].message)