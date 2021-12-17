# FOLDERS
origin_folder = "Data"
processed_data_folder = "Processed Data"
interest_folder = "Interest"
similarities_folder = "Similarities"
raw_data_folder = "Raw Data"

# FILES
raw_purchase_data_filename = "customerid_productid_cntdorderid_filtertannicoit.tsv"
processed_purchase_data_filename = "customerid_productidlast_cntorderid_filtertannicoit.csv"
users_interest_filename = "users_interest.csv"
similarities_destination_filename = "items_similarities_cosine_interest_tannicoit_2.csv"
mapping_product_id_last_filename = "productid_productidlast.tsv"


# PATHS
raw_purchases_path = f"{origin_folder}/{raw_data_folder}/{raw_purchase_data_filename}"
mapping_product_id_last_path = f"{origin_folder}/{raw_data_folder}/{mapping_product_id_last_filename}"
processed_purchases_path = f"{origin_folder}/{processed_data_folder}/{processed_purchase_data_filename}"
interest_path = f"{origin_folder}/{interest_folder}/{users_interest_filename}"
similarities_path = f"{origin_folder}/{similarities_folder}/{similarities_destination_filename}"

