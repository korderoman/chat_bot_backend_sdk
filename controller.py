from agent_simple_chat import AgentSimpleChat
from agent_simple_with_rag import AgentSimpleWithRag
import os

agent_simple_chat=AgentSimpleChat()
agent_simple_chat_with_rag=AgentSimpleWithRag()

file_path=os.path.dirname(os.path.abspath(__file__))+"/documentation/"

def get_message_from_simple_chat(message:str)->str:
    response=agent_simple_chat.get_message(message)
    return response

def load_document():
    agent_simple_chat_with_rag.load_document(f"{file_path}ODS-FINAL210716.pdf")

def get_message_from_simple_chat_with_rag(message:str)->str:
    return get_message_from_simple_chat_with_rag(message)