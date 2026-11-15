from langchain_huggingface import HuggingFacePipeline
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research Tool")

@st.cache_resource
def load_model():
    return HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "max_new_tokens": 100,
            "temperature": 0.7,
        },
    )


llm = load_model()



user_input = st.text_input("Enter your prompt")
# template
template = PromptTemplate(
    
    template="""You are a helpful AI assistant.
please tell about the question "{question}" in simple word    

Answer the following question in one Long sentence.

Answer:"""


)
prompt = template.invoke({"question": user_input})

if st.button("Summarize"):
    
    result = llm.invoke(prompt)
    st.write(result)  



