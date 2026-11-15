from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path= r"C:\Users\ADMIN\Desktop\LangChainModel\venv\Books",
    glob = "*.pdf",
    loader_cls=PyPDFLoader
)

# Load concept
docs = loader.load()

# print(len(docs))
# print("strating the page fron after this")
# print(docs[120].page_content)
# print("metadate of the first page")
# print(docs[0].metadata)


# for documents in docs:
#     print(documents.metadata)/

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
    


