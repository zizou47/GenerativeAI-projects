import pandas as pd 
from langchain_core.documents import Document


def data_converter():
    product_data = pd.read_csv('../data/flipkart_product_review.csv')

    data = product_data[['product_title', 'review']]

    product_list = []

    # iterate over the rows of DF

    for index, row in data.iterrows():
        obj = {

            'product_name': row ['product_title'],
            'review': row['review']
        }

        product_list.append(obj)


    docs = []

    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content= entry['review'], metadata=metadata)
        docs.append(doc)
    return docs