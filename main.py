from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import Pinecone
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os
#
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.environ.get("PINECONE_ENVIRONMENT")

print(PINECONE_API_KEY)
print(PINECONE_ENVIRONMENT)

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

# # index = VectorstoreIndexCreator(vectorstore_cls=Pinecone).from_loaders([CSVLoader("Dummy minutes.csv", encoding="utf-8")])
#
#
# '''sub_docs = self.text_splitter.split_documents(documents)
#         vectorstore = self.vectorstore_cls.from_documents(
#             sub_docs, self.embedding, **self.vectorstore_kwargs
#         )'''
#
docs = CSVLoader("Dummy minutes.csv", encoding="utf-8").load()
sub_docs = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0).split_documents(docs)
vectorstore = Pinecone.from_documents(sub_docs, OpenAIEmbeddings(), index_name="qima")

# vectorstore = Pinecone.from_existing_index(index_name="qima", embedding=OpenAIEmbeddings())
#
# index2 = VectorStoreIndexWrapper(vectorstore=vectorstore)

# result = index.query_with_sources("", chain_type="refine")



# while True:
#     query = input("Enter your query: ")
#     result = index2.query_with_sources(query, chain_type="refine")
#     print(result["answer"])
#     print(result)
