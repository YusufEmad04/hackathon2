from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import Pinecone
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os
import streamlit as st


@st.cache_resource
def get_model():
    print("getting model _________________")

    PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT = os.environ.get("PINECONE_ENVIRONMENT")
    #
    # print(PINECONE_API_KEY)
    # print(PINECONE_ENVIRONMENT)

    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

    vector_store = Pinecone.from_existing_index(index_name="qima", embedding=OpenAIEmbeddings())

    index = VectorStoreIndexWrapper(vectorstore=vector_store)

    return index
