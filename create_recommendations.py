import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from tqdm import tqdm
from strings import *
from defines import *


def compute_recommendations():
    interest_data = pd.read_csv(interest_path)

    # COSTRUISCO LA MATRICE UTENTI-PRODOTTI
    customers_index = interest_data['Customer_ID'].unique().tolist()
    products_index = interest_data['Product_ID_Last'].unique().tolist()

    customers_index_d = {item: idx for idx, item in enumerate(customers_index)}
    products_index_d = {item: idx for idx, item in enumerate(products_index)}
    customers = interest_data['Customer_ID'].values
    products = interest_data['Product_ID_Last'].values
    interests = interest_data['Interest']

    customers_dimension = [customers_index_d.get(item) for item in customers]
    products_dimension = [products_index_d.get(item) for item in products]

    csr_data = csr_matrix((interests, (products_dimension, customers_dimension)),
                          shape=(max(products_dimension) + 1, max(customers_dimension) + 1))
    cosine_similarities = cosine_similarity(csr_data)

    """
        dot_similarities = csr_data.dot(csr_data.transpose())
        dot_similarities = dot_similarities.toarray()

        Non riesco nè a fare calcoli, nè a salvare i file senza usare le matrici csr
        cosine_csr = csr_matrix(cosine_similarities)
        dot_csr = csr_matrix(dot_similarities)

        CREO IL DATAFRAME PRONTO PER L'UPLOAD SU TRACKING
        Per ogni prodotto mi recupero i 10 prodotti più simili e li vado a salvare nel DataFrame
    """
    # Mi serve la lista degli ID dei prodotti
    # perchè avendo lavorato con csr, le similarità corrispondono agli indici, ma non agli ID di questo dictionary
    products_keys = list(products_index_d.keys())
    products_link = []

    for product_index in tqdm(range(cosine_similarities.shape[0])):  # Ciclo su ogni riga delle similarità
        product_1 = products_keys[product_index]
        row = cosine_similarities[product_index]
        sorted_products_index = np.argsort(row)[::-1][1:TOP_N_CONSIGLI + 1]
        sorted_ratios = np.sort(row)[::-1][1:TOP_N_CONSIGLI + 1]
        similar_products_ids = [products_keys[x] for x in sorted_products_index]
        for product_2, rating in zip(similar_products_ids, sorted_ratios):
            if rating > 0:  # Aggiungo solo le similarità maggiori di 0, altrimenti sarebbero similarità false
                products_link.append([product_1, product_2, rating])

    products_link_df = pd.DataFrame(products_link, columns=["product_id", "linked_product_id", "rating"])

    products_link_df["version"] = 1
    products_link_df["model"] = "cosine_interest_tannicoit"

    products_link_df.to_csv(similarities_path, index=False)
