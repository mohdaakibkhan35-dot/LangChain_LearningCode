from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv() 

llm = HuggingFaceEndpoint( 
    repo_id= "meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=100
) 

model = ChatHuggingFace(llm = llm) 

# first Template

template1 = PromptTemplate(
    template= "write the detial  note on {input_data}",
    input_variables=["input_data"]
) 

template2 = PromptTemplate(
    template= "write the Physical,quality,Pros,Cons on the following text {data}",
    input_variables=["data"]
) 

parser = StrOutputParser() 


# This the pipeline of LangChain
chain = template1 | model | parser | template2 | model | parser

user_input = input(" enter the data which you want: "+"")
answer = chain.invoke({'input_data': user_input})

print(answer) 


 
