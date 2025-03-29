import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# load api key for large language model

token = os.environ["GITHUB_TOKEN"]

# create a chatbot instance

llm = ChatOpenAI(temperature=0, model_name="gpt-4o")


# create prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a intelligent chatbot. Answer the following questions."),
        ("user", "{question}"),



    ]
)