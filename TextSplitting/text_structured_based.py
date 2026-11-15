from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
In Python, a variable is a name that refers to an object stored in memory, aka an object reference, so Python
uses a pass-by-object-reference system. If an argument is changed in a function, the changes are kept or lost
depending on the object's mutability.
A mutable object can be modified after creation. A function's changes to
the object then appear outside the function. An immutable object cannot be modified after creation. So a
function must make a local copy to modify, and the local copy's changes don't appear outside the function.
Programmers should be cautious of modifying function arguments as these side effects can make programs
difficult to debug and maintain. 
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 250,
    chunk_overlap = 0,
)
chunks = splitter.split_text(text)
print("chunk Size")
print(len(chunks))
# print(chunks)


