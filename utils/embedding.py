from langchain.embeddings import HuggingFaceEmbeddings
from pdf_loading import load_pdf
from text_splitter import split_pages
from langchain_community.vectorstores import Chroma


pdf_path = "C:/Users/hp/desktop/RAG-CV-Chatbot/data/pdf/data.pdf"

pages = load_pdf(pdf_path)
chunks = split_pages(pages)




embedding_model = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [chunk.page_content for chunk in chunks]


embeddings = embedding_model.embed_documents(texts)

print(f"number of texts : {len(texts)}")
print(f"number of embeddings : {len(embeddings)}")



