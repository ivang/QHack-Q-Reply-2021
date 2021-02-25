import pandas as pd
from typing import Tuple


def load_data(filename: str) -> pd.DataFrame:
    df = pd.read_csv("data/{}".format(filename))
    return df


def load_train_test(filename: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Apply train-test split.
    Rescale numerical features to have mean=0 and std=1.
    
    """
    df = load_data(filename)  
    #Sample
    train_df = df.sample(frac=0.8, random_state=42)
    test_df = df[~df.index.isin(train_df.index)]
    #Rescale
    train_mean = train_df.iloc[:, :-1].mean()
    train_std = train_df.iloc[:, :-1].std()
    train_df.iloc[:, :-1] = (train_df.iloc[:, :-1] - train_mean) / train_std
    test_df.iloc[:, :-1] = (test_df.iloc[:, :-1] - train_mean) / train_std
    return train_df, test_df


def load_train_test_pca(n_components: int, filetag: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load a PCA-transformed version of the data.
    Return only the desired number of components.
    
    """
    #Sample
    train_df = pd.read_csv("data/{}_pca_transformed_train.csv".format(filetag))
    test_df = pd.read_csv("data/{}_pca_transformed_test.csv".format(filetag))
    #Select
    columns = [f"pca_{j}" for j in range(1, n_components + 1)] + ["label"]
    return train_df[columns], test_df[columns]
