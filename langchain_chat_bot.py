import os
from langchain_openai import ChatOpenAI

token = os.environ["GITHUB_TOKEN"]


llm = ChatOpenAI(token=token, model_name="gpt-4o")