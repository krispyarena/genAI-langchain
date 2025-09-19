from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 300)

docs = [
    "Kathmandu is the capital of Nepal",
    "Paris is the capital of France",
    "Berlin is the capital of Germany",
    "Cape Town is the capital of South Africa",
    "Seoul is the capital of South Korea"
]

query = "Tell me about South Korea"

doc_embedding = embedding.embed_documents(docs)
qry_embedding = embedding.embed_query(query)

scores = cosine_similarity([qry_embedding], doc_embedding)[0]

list1 = list(enumerate(scores))

index, score = sorted(list1 , key = lambda x:x[1])[-1]

print(query)
print(docs[index])
print('Similarity score : ', score)
