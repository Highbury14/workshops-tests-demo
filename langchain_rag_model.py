# my google-colab file: https://colab.research.google.com/drive/1zHXsACFr8OyaFczt5NLpw5Zkp4eszTSH

# # Fetch the provided context .txt file and copy it to this local-environment.

from google.colab import auth
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload

# 1. Authenticate your account session
auth.authenticate_user()
drive_service = build('drive', 'v3')

# 2. Input the shared File ID
file_id = '1pBXd2LLKniKW4xa7LRcnUhRiLeSKzAEQEgN6ejLoWHM'
# context-file gdrive-link: https://docs.google.com/document/d/1pBXd2LLKniKW4xa7LRcnUhRiLeSKzAEQEgN6ejLoWHM

# 3. Instruct Google to export the .gdoc directly as plain text
request = drive_service.files().export_media(fileId=file_id, mimeType='text/plain')
file_stream = io.BytesIO()
downloader = MediaIoBaseDownload(file_stream, request)

# 4. Stream the data chunks into memory
done = False
while done is False:
    status, done = downloader.next_chunk()

# 5. Decode the raw bytes into a Python string
text_content = file_stream.getvalue().decode('utf-8')

# 6. Save it as a genuine local text file inside Colab
output_path = '/content/converted_technova_policy.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text_content)

# 3. Stream and save the file directly to Colab local files
# request = drive_service.files().get_media(fileId=shared_file_id)
# downloaded_file = io.BytesIO()
# downloader = MediaIoBaseDownload(downloaded_file, request)

# 5. Save the downloaded bytes as a file in your environment
# downloaded_file.seek(0)
# with open('/content/technova_policy.txt', 'wb') as f:
    # f.write(downloaded_file.read())

# print("Success! File downloaded.")
#  to /content/shared_file.txt")

# print(f"Success! File converted and saved locally to: {output_path}")

# # Instantiate the Langchain LLM-model object

!pip install -q langchain langchain-core langchain-community

!pip install -q langchain-groq langchain-huggingface sentence-transformers faiss-cpu pypdf

from google.colab import userdata
from langchain_groq import ChatGroq

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    api_key = userdata.get("GROQ_API_KEY")
)

llm

# # Using the saved .txt file

from langchain_community.document_loaders import TextLoader
# WebBaseLoader

loader = TextLoader("/content/converted_technova_policy.txt")
# WebBaseLoader("https://docs.google.com/document/d/1pBXd2LLKniKW4xa7LRcnUhRiLeSKzAEQEgN6ejLoWHM")

docs1 = loader.load()

docs1

docs1[0].page_content.strip("\ufeff")

# # Split

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size = 50, chunk_overlap = 15)

chunks = splitter.split_documents(docs1)

# # Embeddings

from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

# # Store embeddings in a vectorDB

from langchain_community.vectorstores import FAISS
vectorstore = FAISS.from_documents(chunks, embedding_model)

# ## Create retriever

retriever = vectorstore.as_retriever(search_kwargs = {"k": 3})

# # Create RAG chain

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def format_docs(docs):
  return "\n\n".join(doc.page_content for doc in docs)

template = """
Use the following context to answer the question.
Use three sentences maximum and keep the answer concise.
If the information needed to answer the question is not present in the given context data, then answer that the document does not provide this information.
Don't invent any new information not present in the given context data, to answer the question.

Context: {context}

Question: {question}

Answer:
"""

prompt = PromptTemplate.from_template(template)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

query1 = "How many paid annual leave days does a full-time employee receive per year ?"

response = rag_chain.invoke(query1)
response
# 'A full‑time employee receives **18 paid annual leave days per year**.'

query2 = "An employee wants to work remotely on Wednesday and take leave on Friday. What do the company policies say about these two requests ?"

response = rag_chain.invoke(query2)
response
# 'The policy permits remote work on Wednesdays, so the employee’s request to work remotely that day is allowed. It also allows employees to work remotely up to three calendar days before a requested leave, which covers Wednesday when the leave is on Friday. The document does not place any restriction on taking leave on Friday, so that request is also permissible.'

query3 = "What is the company's parental leave policy ?"

response = rag_chain.invoke(query3)
response
# 'The document does not provide information about the company's parental leave policy.'

query4 = "When and where was Acme Inc. founded?"
# "What new product line was launched in 2024 in Acme Inc?"

response = rag_chain.invoke(query4)
response
# 'The document does not provide this information.'

"""
# query1 = "How many paid annual leave days does a full-time employee receive per year ?"
# Answer: 'A full‑time employee receives **18 paid annual leave days per year**.'
# query2 = "An employee wants to work remotely on Wednesday and take leave on Friday. What do the company policies say about these two requests ?"
# Answer: 'The policy permits remote work on Wednesdays, so the employee’s request to work remotely that day is allowed. It also allows employees to work remotely up to three calendar days before a requested leave, which covers Wednesday when the leave is on Friday. The document does not place any restriction on taking leave on Friday, so that request is also permissible.'
# query3 = "What is the company's parental leave policy ?"
# Answer: 'The document does not provide information about the company's parental leave policy.'
# query4 = "When and where was Acme Inc. founded?"
# Answer: 'The document does not provide this information.'
"""

# from google.colab import drive
# drive.mount('/content/drive')

# !cp "/content/drive/MyDrive/Copy_of_technova_policy.txt" "/content/"

# Replace 'shared_file.txt' with the exact name of the file
# with open('/content/drive/MyDrive/Copy_of_technova_policy.txt.gdoc') as file:
    # content = file.read()
    # print(content)

# response = llm.invoke("What is langchain? Answer in one paragraph only")
# response.content

# response = llm.invoke("What new product line was launched in 2024 in Acme Inc?")
# print(response.content)

# response = llm.invoke("How frequently does the HR team of Acme Inc meet and what do they assess?")
# print(response.content)

# RAG

# 1. Load the documents for retrieval.
# 2. Split the documents
# 3. Produce embeddings for each of the splits
# 4. Store the embeddings in a vectorDB
# 5. Create a retriever to retrieve the embeddings from the VectorDB
# 6. Combine the LLM and the retriever and produce results.

# Document

# from langchain_core.documents import Document

# doc1 = Document(page_content = "This is the first document.", metadata = {"source": "first_file"})

# doc1

# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader("RAG_file.pdf")

# docs2 = loader.load()

# docs2

# CSVLoader
# UnstructuredHTMLLoader

# all_docs = doc1 + docs2 + .....

# chunks

# print(splitter._chunk_size)
# print(splitter._chunk_overlap)

# vectors = embedding_model.embed_documents([doc.page_content for doc in chunks])

# len(vectors)

# len(vectors[0])

# vectorstore

# retrieved_docs = vectorstore.similarity_search("What was the launch date?", k = 2)
# retrieved_docs

# retrieved_docs = vectorstore.similarity_search_with_score("What was the launch date?", k = 5)
# retrieved_docs

# retriever.invoke("What was the launch date?")
