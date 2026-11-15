from langchain_community.retrievers import WikipediaRetriever

# intialize the retriver(optional: set language and top k)

retriever = WikipediaRetriever(
    top_k_results=2,
    lang = "en"
)

# define the query
query = "the geopolitical history of india and pakistan and china"


# get relevent wikipedia documents
docs = retriever.invoke(query)


# Print retrive document 
for i , doc in enumerate(docs):
    print(f"\n---- Result {i+1}--")
    print(f"Content\n{doc.page_content}...") 
    