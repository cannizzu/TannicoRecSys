from data_loading import *
from create_recommendations import *
from compute_interest import *

if __name__ == '__main__':
    print("Loading data...")
    load_data()
    print("Computing interest...")
    compute_users_interest()
    print("Computing recommendations...")
    compute_recommendations()
    print("FATTO STRONZI")

