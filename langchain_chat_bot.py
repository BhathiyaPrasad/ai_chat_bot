import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from lancchain_core.output_parser import StringOutputParser

from app import response

# load api key for large language model

token = os.environ["GITHUB_TOKEN"]
parser = StringOutputParser()
# create a chatbot instance

llm = ChatOpenAI(temperature=0, model_name="gpt-4o")


# create prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a intelligent chatbot. Answer the following questions."),
        ("user", "{question}"),



    ]
)

chain = prompt | llm | parser


question = "My name is Bhathiya Prasad"

response = chain.invoke({"question": question})

print(response)