from langchain_core.prompts import ChatPromptTemplate

chatTemplate = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain about {topic} in simple terms')
])

prompt = chatTemplate.invoke({'domain' : 'Football', 'topic' : 'Offside'})

print(prompt)
