# # Precedentemente sono state eseguite due query:
# 1) Estrazione di Customer_ID, Product_ID, Count (distinct Order_ID)
#       => Serve a recuperare l'"interesse" (numero di ordini) di un utente verso un determinato prodotto
# 2) Estrazione della mappatura Product_ID, Product_ID_LAST, is_in_catalog
#       => Serve a raggruppare l'interesse per prodotti specifici
#       secondo il Product_ID_LAST Entrambe le query sono salvate sotto "Queries/get_raw_data.txt"
import pandas as pd
from strings import *


def load_data():
    user_product_n_orders = pd.read_csv(raw_purchases_path, sep="\t")
    product_id_product_id_last = pd.read_csv(mapping_product_id_last_path, sep="\t")[['Product_ID', 'Product_id_LAST']]

    # Adesso creo il frame che unisce i dati raggruppando per product_id_LAST => se non lo facessimo, ci troveremmo che
    # due prodotti di annate diverse risultano prodotti diversi
    joined_frame = user_product_n_orders.merge(product_id_product_id_last, on="Product_ID")[
        ['Customer_ID', 'Product_id_LAST', 'count_order']]

    nan_counter = joined_frame['Product_id_LAST'].isna().sum()
    if nan_counter > 0:
        print(f"N° prodotti che non ho trovato nel file di mapping con il product_id_LAST: {nan_counter}")

    joined_frame = joined_frame.groupby(["Customer_ID", "Product_id_LAST"]).sum().reset_index()

    # Adesso salviamo i dati
    joined_frame.to_csv(processed_purchases_path, index=False)
