import pandas as pd
from langchain_core.documents import Document

def dataconverter():
    # Load product review data from CSV
    product_data = pd.read_csv('./data/flipkart_product_review.csv')

    # Select relevant columns
    data = product_data[['product_title', 'review']]

    product_list = []

    # Iterate over rows to create a list of dictionaries
    for index, row in data.iterrows():
        obj = {
            'product_name': row['product_title'],
            'review': row['review']
        }
        product_list.append(obj)

    # Create a list of Document objects for Hugging Face input
    docs = []
    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content=entry['review'], metadata=metadata)
        docs.append(doc)

    return docs
