from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\ADMIN\Desktop\LangChainModel\venv\Books")
docs = loader.load()
print(type(docs))
print("length of the pdf", len(docs))
print(docs[24].metadata)

