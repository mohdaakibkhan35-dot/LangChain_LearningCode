from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.amazon.in/Apple-2026-MacBook-Laptop-chip/dp/B0GR64G4H6/ref=asc_df_B0GR64G4H6?mcid=4f9bf6da8f2f350eae922e4cbb87056c&tag=googleshopdes-21&linkCode=df0&hvadid=794212938611&hvpos=&hvnetw=g&hvrand=18360762046238021412&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9183229&hvtargid=pla-2470150962883&hvocijid=18360762046238021412-B0GR64G4H6-&hvexpln=0&gad_source=1&th=1'
loader = WebBaseLoader(url)
docs = loader.load()
print(len(docs))
print(docs[0].page_content)



