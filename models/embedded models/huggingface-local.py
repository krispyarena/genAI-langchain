from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

docs = [
    "Kathmandu is the capital of Nepal",
    "Berlin is the capital of Germany",
    "Moscow is the capital of Russia"
]

vector = em.embed_documents(docs)

print(str(vector))
