from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# instanciando embeddings e llm
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", max_tokens=500)

# carregando o documento e dividindo em partes
document_link = "./duvidas_sg.docx"
loader = Docx2txtLoader(document_link)
document = loader.load_and_split()

# separar os chunks splitters (criando o menor child e o maior parent)
child_splitter = RecursiveCharacterTextSplitter(chunk_size=200)

parent_splitter = RecursiveCharacterTextSplitter(
    chunk_size=4000, chunk_overlap=200, length_function=len, add_start_index=True
)

# vector storage
store = InMemoryStore()

vectorstore = Chroma(embedding_function=embeddings, persist_directory="childVectorDB")

# executando o retriever
parente_document_retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)

parente_document_retriever.add_documents(document, ids=None)

# print(parente_document_retriever.vectorstore.get())

TEMPLATE = """
    Você é um especialista em educação a distância. Responda as perguntas utilizando o contexto informado.
    
    Query:
    {question}
    
    Context:
    {context}
"""

rag_prompt = ChatPromptTemplate.from_template(TEMPLATE)

setup_retrieval = RunnableParallel(
    {"question": RunnablePassthrough(), "context": parente_document_retriever}
)

output_parser = StrOutputParser()

parent_chain_retrieval = setup_retrieval | rag_prompt | llm | output_parser


while True:
    print("Digite sua pergunta, e para encerrar o chat digite 2:")
    question = input()
    if question == "2":
        print("Chat encerrado.")
        break
    elif():
        continue
    else:
        response = parent_chain_retrieval.invoke(question)
        print("\n",response,"\n")