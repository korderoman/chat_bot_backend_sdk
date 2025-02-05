from langchain import hub
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import SKLearnVectorStore

from dotenv import load_dotenv

load_dotenv()


class AgentSimpleWithRag:
    def __init__(self):
        self.chat=ChatOpenAI(temperature=0)
        self.loader=None
        self.docs=None
        self.docs_split=None
        self.text_splitter=CharacterTextSplitter(chunk_size=1024,chunk_overlap=200)
        self.embeddings=OpenAIEmbeddings()
        self.vector_store=None
        self.qa=None
    def count_tokens(self):
        """
        Cuenta el número de tokens en el documento
        :return: El número de tokens
        """
        full_text="".join([doc.page_content for doc in self.docs])
        return len(full_text.split())

    def split_document(self):
        self.docs_split=self.text_splitter.split_documents(self.docs)
        print(len(self.docs_split))

    def implement_rag(self, file_path):
        self.load_document(file_path)
        self.split_document()
        self.save_embeddings_in_vectorial_database()
        self.load_save_embeddings_in_vectorial_database()
        self.start_qa()


    def save_embeddings_in_vectorial_database(self):
        self.vector_store=SKLearnVectorStore.from_documents(
            documents=self.docs_split,
            embedding=self.embeddings,
            persist_path="./ods_embeddings",
            serializer="parquet"
        )
        self.vector_store.persist()

    def load_save_embeddings_in_vectorial_database(self):
        self.vector_store=SKLearnVectorStore(
            persist_path="./ods_embeddings",
            serializer="parquet",
            embedding=self.embeddings
        )
    def start_qa(self):
       prompt=hub.pull("langchain-ai/retrieval-qa-chat")
       combine_docs_chain=create_stuff_documents_chain(self.chat,prompt)
       self.qa=create_retrieval_chain(
           retriever=self.vector_store.as_retriever(),
           combine_docs_chain=combine_docs_chain

       )


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
        #print(len(self.docs[40].page_content.split()))
        #Se imprime el contenido de la página 41 de nuestro documento pdf (opcional)
        #print(self.docs[40].page_content)

    def get_message(self,message:str)->str:
        result=self.qa.invoke(input={'input':message})
        print(result)
        return result['answer']