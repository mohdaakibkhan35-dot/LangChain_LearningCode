from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    max_new_tokens=100
) 
model = ChatHuggingFace(llm=llm) 
input_value = input("enter the value:" + " ")


#input_data = input("aap ko kya puchna hai:/n"+" ")
template1 = PromptTemplate(
    template="write a detialed report on {input_query}",
    input_variables=['input_query']

) 
text = template1.invoke({'input_query':input_value})
model_first_answer = model.invoke(text)

prompt2 = PromptTemplate(
    template="write a five line summary on the following text {model_first_answer}",
    input_variables= ['model_first_answer']

) 

text2 = prompt2.invoke({'model_first_answer':model_first_answer.content})
answer = model.invoke(text2)
print(answer.content)




