from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
load_dotenv()


class AgentSimpleWithRag:
    def __init__(self):
        self.chat=ChatOpenAI(temperature=0)
        self.loader=None
        self.docs=None

    def count_tokens(self):
        """
        Cuenta el número de tokens en el documento
        :return: El número de tokens
        """
        full_text="".join([doc.page_content for doc in self.docs])
        return len(full_text.split())

    def load_document(self,file_path):
        """
        Carga el documento pdf
        :param file_path: Ruta del archivo pdf en nuestro local
        :return:
        """
        self.loader=PyPDFLoader(file_path)
        self.docs=self.loader.load()
        #Se imprime el número total de tokens del documento
        print(f"raw tokens: {self.count_tokens()}")
        #Se imprime el contenido de la página 41 de nuestro documento pdf (opcional)
        print(len(self.docs[40].page_content.split()))
        #Se imprime el contenido de la página 41 de nuestro documento pdf (opcional)
        print(self.docs[40].page_content)

    def get_message(self,message:str)->str:
        response=self.chat.invoke(message)
        return response.content