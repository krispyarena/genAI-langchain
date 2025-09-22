from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chat Template
chatTemplate = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

# Load Chat History

chat_history = []

with open('chatHistory.txt') as f:
    chat_history.extend(f.readlines())

# Create Prompt
prompt = chatTemplate.invoke({'chat_history':chat_history, 'query':'Where is my refund?'})

print(prompt)
