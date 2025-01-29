import langchain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat=ChatOpenAI(temperature=0)

def get_message_from_open_ai(message:str)->str:
    response=chat.invoke(message)
    return response.content