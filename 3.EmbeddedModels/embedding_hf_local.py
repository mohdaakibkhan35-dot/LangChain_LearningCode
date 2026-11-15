from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
test = "Delhi is the Capital of india"

vector = embedding.embed_query(test)
print(str(vector))


document = [
    "delhi is the capital of india",
    "kolkata is the capital of west bengal",
    "paris is the capital of France"   
]

vectors = embedding.embed_documents(document)
print(str(vectors))