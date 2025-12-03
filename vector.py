import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

import os

df = pd.read_csv("Amazon_Unlocked_Mobile.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chome_langchain_db"
add_documents = not os.path.exists(db_location)


if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        # Convert all values to strings and handle NaN values
        product_name = str(row["Product Name"]) if pd.notna(row["Product Name"]) else ""
        brand_name = str(row["Brand Name"]) if pd.notna(row["Brand Name"]) else ""
        reviews = str(row["Reviews"]) if pd.notna(row["Reviews"]) else ""
        price = str(row["Price"]) if pd.notna(row["Price"]) else ""
        
        page_content = f"{product_name} {brand_name} {reviews} {price}".strip()
        
        document = Document(
            page_content=page_content,
            metadata={
                "rating": int(row["Rating"]) if pd.notna(row["Rating"]) else 0,
                "date": str(row["Review Votes"]) if pd.notna(row["Review Votes"]) else ""
            },
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
vector_store = Chroma(
    collection_name="mobile_phone_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)