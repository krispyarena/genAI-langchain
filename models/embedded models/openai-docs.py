from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

e = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

docs = [
    "Kathmandu is the capital of Nepal",
    "Berlin is the capital of Germany",
    "Moscow is the capital of Russia"
]

result = e.embed_documents(docs)

print(str(result))
