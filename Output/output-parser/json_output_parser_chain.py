from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv() 


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=2,
    max_new_tokens=100
) 

model = ChatHuggingFace(llm = llm) 
parser = JsonOutputParser()

template = PromptTemplate(
    template="write the physical Note about the person like age,height {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
) 


parser = JsonOutputParser()

chain = template | model | parser

final_result = chain.invoke()


print(type(final_result))
print()
print(final_result)



