from langchain_community.document_loaders import TextLoader

loader = TextLoader(r"C:\Users\ADMIN\Downloads\rocket_technology_space_exploration.txt",encoding='utf-8')
docs = loader.load()


print("type of docs",type(docs))
# print("Page content of document",docs[0].page_content)
print("page metadata of document",docs[0].metadata)

