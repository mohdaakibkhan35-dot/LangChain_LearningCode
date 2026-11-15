from dotenv import load_dotenv
from huggingface_hub import InferenceClient
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    provider="hf-inference"
)

response = client.chat_completion(
    model="HuggingFaceTB/SmolLM3-3B",
    messages=[
        {"role": "user", "content": "What is the capital of India?"}
    ],
    max_tokens=100
)

print(response.choices[0].message.content) 