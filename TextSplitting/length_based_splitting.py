from langchain_text_splitters import CharacterTextSplitter

text = """
In Python, a variable is a name that refers to an object stored in memory, aka an object reference, so Python
uses a pass-by-object-reference system. If an argument is changed in a function, the changes are kept or lost
depending on the object's mutability. A mutable object can be modified after creation. A function's changes to
the object then appear outside the function. An immutable object cannot be modified after creation. So a
function must make a local copy to modify, and the local copy's changes don't appear outside the function.
Programmers should be cautious of modifying function arguments as these side effects can make programs
difficult to debug and maintain. 
"""

basic_splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0,
    separator = ''
)

result = basic_splitter.split_text(text)
# print(result)


# using document loader and text+splitter

print("output of the document_splitter "+ """                             """)


from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader(r"C:\Users\ADMIN\Downloads\rocket_technology_25_pages.pdf")
docs = loader.load()

document_splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)
result1 = document_splitter.split_documents(docs)
print("PAGE CONTENT",result1[10].page_content)
print("METADATA" , result1[10].metadata)



