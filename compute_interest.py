import pandas as pd
from strings import *


# CREAZIONE DATASET DEGLI ACQUISTI BASATO SUGLI INTERESSI (interesse = [0,1]) - Righe: Utenti - Colonne: Nomi dei
# prodotti (rimossa l'annata, così da raggruppare gli acquisti indipendentemente dall'anno della bottiglia) -
# Contenuto: Preferenza (numero di ordini effettuati dall'utente per ogni prodotto)
def compute_users_interest():
    # PULISCO I DATI PER PORTARLI IN FORMA MATRICIALE
    processed_data_df = pd.read_csv(processed_purchases_path)
    processed_data_df.columns = ['Customer_ID', 'Product_ID_Last', 'Orders_Count']

    # Scalo i valori di Orders_Count per ogni utente per avere valori tra 0 e 1
    max_n_orders = processed_data_df.groupby("Customer_ID").max("Orders_Count").reset_index()[
        ['Customer_ID', "Orders_Count"]]
    processed_data_df = processed_data_df.merge(max_n_orders, on="Customer_ID", how="left")
    processed_data_df['Interest'] = processed_data_df['Orders_Count_x'] / processed_data_df['Orders_Count_y']
    processed_data_df = processed_data_df[['Customer_ID', 'Product_ID_Last', 'Interest']]
    processed_data_df.to_csv(interest_path, index=False)
