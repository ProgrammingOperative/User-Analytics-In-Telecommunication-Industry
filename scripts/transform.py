import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer, MinMaxScaler


class Transform:
    def __init__(self, df) -> None:
        self.df = df


def find_agg(self, agg_column:str, agg_metric:str, col_name:str, top:int, order=False )->pd.DataFrame:
    
    new_df = self.df.groupby(agg_column)[agg_column].agg(agg_metric).reset_index(name=col_name).\
        sort_values(by=col_name, ascending=order)[:top]
    """
    Parameters:
    
    agg_column - The column from which the dataframe is to be aggregated from
    agg_metric - Function to aggregate this column
    col_name   - Name of the new column created containing aggregated values per agg_column
    top        - Number of records to be dislayed
    order      - True for ascending and False for 
    
    
    reset_index, creates a new column which is named after the col_name parameter hence this creates a dataframe 
                with 2 columns which allows for sorting using a particular column. This new column also works 
                as the new index"""
    return new_df


def convert_bytes_to_megabytes(self, bytes_data):
    """
        This function takes the dataframe and the column which has the bytes values
        returns the megabytesof that value
        
        Args:
        -----
        df: dataframe
        bytes_data: column with bytes values
        
        Returns:
        --------
        A series
    """
    
    megabyte = 1*10e+5
    self.df[bytes_data] = self.df[bytes_data] / megabyte
    return self.df[bytes_data]


def fix_outlier(self, column):
    self.df[column] = np.where(self.df[column] > self.df[column].quantile(0.95), self.df[column].median(),self.df[column])
    
    return self.df[column]

    """
    Values outside the 0.95 quantile range are treated as outliers and converted to the median
    """


def scaler(self):
    minmax_scaler = MinMaxScaler()
    scaled_data = minmax_scaler.fit_transform(self.df)

    # plot both together to compare
    fig, ax = plt.subplots(1,2, figsize=(10, 6))
    sns.histplot(self.df, ax=ax[0])
    ax[0].set_title("Original Data")
    sns.histplot(scaled_data, ax=ax[1])
    ax[1].set_title("Scaled data")

    """
    This function takes as input the dataframe and scales then it then plots a comparison 
    between the original data and scaled version of the same"""


def normalizer(self):
    norm = Normalizer()
    # normalize the exponential data with boxcox
    normalized_data = norm.fit_transform(self.df)

    # plot both together to compare
    fig, ax=plt.subplots(1,2, figsize=(10, 6))
    sns.histplot(df, ax=ax[0])
    ax[0].set_title("Original Data")
    sns.histplot(normalized_data[0], ax=ax[1])
    ax[1].set_title("Normalized data")