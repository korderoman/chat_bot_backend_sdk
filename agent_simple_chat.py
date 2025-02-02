from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
class AgentSimpleChat:
    def __init__(self):
        self.chat=ChatOpenAI(temperature=0)

    def get_message(self,message:str)->str:
        response=self.chat.invoke(message)
        return response.content