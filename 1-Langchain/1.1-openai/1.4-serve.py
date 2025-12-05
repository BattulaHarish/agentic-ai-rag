from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()
from langserve import add_routes
groq_api_key = os.getenv("GROQ_API_KEY")
model=ChatGroq(model="openai/gpt-oss-20b",groq_api_key=groq_api_key)

# Prompt template
from langchain_core.prompts import ChatPromptTemplate

system_template="Translate the language from {language}"
prompt=ChatPromptTemplate.from_messages(
    [("system",system_template),("user","{text}")]
)

parser=StrOutputParser()
chain=prompt|model|parser

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using Langchain's Runnable interfaces"
)
add_routes(
    app,
    chain,
    path="/chain"
)
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)