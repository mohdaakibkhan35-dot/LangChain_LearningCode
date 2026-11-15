from langchain_community.tools import DuckDuckGoSearchResults
search_tool = DuckDuckGoSearchResults()

results = search_tool.invoke("capital of all state in india")
print(results)
