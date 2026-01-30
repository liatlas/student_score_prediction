import pandas as pd
from pathlib import Path

DATASET_PATH = Path("../data/raw/train.csv")

def load_train_data():
    return pd.read_csv(DATASET_PATH, index_col='id')
