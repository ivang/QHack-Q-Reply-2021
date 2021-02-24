import pandas as pd
from typing import Tuple


def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/Rice_Osmancik_Cammeo_Dataset.csv")
    return df


def load_train_test() -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = load_data()  
    #Sample
    train_df = df.sample(frac=0.8, random_state=42)
    test_df = df[~df.index.isin(train_df.index)]
    #Rescale
    train_mean = train_df.iloc[:, :-1].mean()
    train_std = train_df.iloc[:, :-1].std()
    train_df.iloc[:, :-1] = (train_df.iloc[:, :-1] - train_mean) / train_std
    test_df.iloc[:, :-1] = (test_df.iloc[:, :-1] - train_mean) / train_std    
    return train_df, test_df
