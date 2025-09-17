from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id='mistralai/Mistral-7B-Instruct-v0.2',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100,
    )
)
model = ChatHuggingFace(llm=llm)

query = "What is the capital of Nepal"
result = model.invoke(query)

print(result.content)
