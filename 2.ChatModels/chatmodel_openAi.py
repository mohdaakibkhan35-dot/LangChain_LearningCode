from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-4.1-mini',temperature=0.3,max_completion_tokens=50)
result = model.invoke("what is tha capital of china")
print(result)
print(result.content)
