from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

e = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

text = "Kathmandu is the capital of Nepal"
result = e.embed_query(text)

print(str(result))