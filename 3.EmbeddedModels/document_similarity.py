from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large',dimensions=300)
documents = [
    
    "Wake up early and start the day with a positive mindset.",
    "Drink enough water to stay healthy.",
    "Exercise for at least 30 minutes every day.",
    "Read a book to improve your knowledge.",
    "Practice coding regularly to build your skills.",
    "Complete important tasks before deadlines.",
    "Learn something new every day.",
    "Take short breaks while working.",
    "Spend quality time with family and friends.",
    "End the day by planning for tomorrow."
]

query = 'tel me about virat kohli'

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

ans = cosine_similarity([query_embedding],doc_embedding)[0]
index,source = sorted(list(enumerate(ans)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similarity_score_is",score)
