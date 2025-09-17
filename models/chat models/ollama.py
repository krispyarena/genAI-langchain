from langchain_ollama import ChatOllama

model = ChatOllama(
    model="mistral",
    temperature=0.5,
)

query = "What is the future of Agentic AI?"

result = model.invoke(query)
print(result.content)
