from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()

index_name = "tes-knowledge-database"  # change if desired

# Load the document, split it into chunks, and embed each chunk.
loader = PyPDFLoader("database/manual_skyrim.pdf")
pages = loader.load_and_split()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = text_splitter.split_documents(pages)

embeddings = OpenAIEmbeddings()
store = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)