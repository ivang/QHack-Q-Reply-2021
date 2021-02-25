import pandas as pd
from typing import Tuple
# from imblearn.over_sampling import SMOTE #importing important libraries for oversampling data
from collections import Counter
from sklearn.model_selection import train_test_split


def load_data(filename: str) -> pd.DataFrame:
    df = pd.read_csv("data/{}".format(filename))
    return df

def kaggle_preprocessing(dat: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    dat=dat[dat['creatinine_phosphokinase']<2000] #removing outliers in creatinine_phosphokinase
    dat=dat[dat['ejection_fraction']<65] #removing outliers in ejection_fraction
    dat=dat[(dat['platelets']>100000) & (dat['platelets']<450000)] #removing outliers in platelets
    dat=dat[dat['serum_creatinine']<2] #removing outliers in serum_creatinine
    dat=dat[dat['serum_sodium']>126] #removing outliers in serum_sodium
    
    x = dat[[c for c in dat.columns if c != 'DEATH_EVENT']] # separating features
    y = dat['DEATH_EVENT'] # separating target
    
    # smote = SMOTE()
    # # fit predictor and target variable
    # x_smote, y_smote = smote.fit_resample(x, y)

    # print('Original dataset shape', Counter(y))
    # print('Resample dataset shape', Counter(y_smote))

    return x, y


def load_train_test(filename: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Apply train-test split.
    Rescale numerical features to have mean=0 and std=1.
    
    """
    df = load_data(filename)
    x, y = kaggle_preprocessing(df)
    #Sample
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)
    #Rescale
    train_mean = X_train[['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']].mean()
    train_std = X_train[['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']].std()
    X_train[['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']] = (X_train[['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']] - train_mean) / train_std
    X_test[['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']] = (X_test[['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']] - train_mean) / train_std
    
    return X_train, X_test, y_train, y_test


def load_train_test_pca(n_components: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load a PCA-transformed version of the data.
    Return only the desired number of components.
    
    """
    #Sample
    train_df = pd.read_csv("data/heart_pca_transformed_train.csv")
    test_df = pd.read_csv("data/heart_pca_transformed_test.csv")
    #Select
    columns = [f"pca_{j}" for j in range(1, n_components + 1)] + ["label"]
    return train_df[columns], test_df[columns]
