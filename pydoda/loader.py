#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np


class Loader:
    """
    The Loader class provides methods to load and work with Doda datasets.
    
    This class allows you to retrieve and explore different categories of Doda datasets, such as
    semantic categories, syntactic categories, and additional extra categories.
    """
    def __init__(self, dataset_dir, category_file_path) -> None:
        self.__dataset = dataset_dir
        self.__category_file = category_file_path
        try:
            self.__df = pd.read_csv(os.path.join(self.__dataset, self.__category_file))
            self.__df = self.__df.replace(np.nan, None)
        except FileNotFoundError:
            raise ValueError('Invalid dataset directory or category file path')
    
    @property
    def columns(self) -> list[str]:
        """
        Returns a list of available columns in the dataset.
        
        Returns:
            A list of available columns in the dataset.
        """
        return self.__df.columns.tolist()
    
    def get_shape(self) -> tuple[int, int]:
        """
        Returns the shape of the dataset.

        Returns:
            A tuple containing the shape of the dataset.
        """
        return self.__df.shape

    def get_column(self, column_name) -> list:
        """
        Returns a list of values in the specified column.
        
        Args:
            column_name: The name of the column to retrieve.
            
        Returns:
            A list of values in the specified column.
        """
        try:
            return self.__df[column_name].tolist()
        except KeyError:
            raise ValueError(f'Invalid column name: {column_name}')
    
    def get_row(self, column, value) -> dict:
        """
        Returns a dictionary containing the values of the specified row.
        
        Args:
            column: The name of the column to search in.
            value: The value to search for.
            
        Returns:
            A dictionary containing the values of the specified row.
        """
        try:
            return self.__df.loc[self.__df[column] == value].to_dict(orient='records')[0]
        except IndexError:
            raise ValueError(f'Invalid value: {value}')
        except KeyError:
            raise ValueError(f'Invalid column name: {column}')
        except ValueError:
            raise ValueError(f'Invalid value: {value}')
    
    def get_word(self, column, value, return_column) -> str:
        """
        Returns the value of the specified column in the specified row.

        Args:
            column: The name of the column to search in.
            value: The value to search for.
            return_column: The name of the column to return the value from.
        
        Returns:
            The value of the specified column in the specified row.
        """
        try:
            return self.__df.loc[self.__df[column] == value, return_column].item()
        except KeyError:
            raise ValueError(f'Invalid columns')
        except ValueError:
            raise ValueError(f'Invalid value: {value}')
    
    def filter_rows_by_string(self, column: str, value: str) -> list[dict[str, str]]:
        """
        Returns a list of dictionaries containing the values of the specified rows.

        Args:
            column: The name of the column to search in.
            value: The value to search for.
        
        Returns:
            A list of dictionaries containing the values of the specified rows.
        """
        try:
            filtered_df = self.__df.loc[self.__df[column].str.contains(value, na=False)]
            filtered_df = filtered_df.infer_objects(copy=False)
            return filtered_df.to_dict(orient='records')
        except KeyError:
            raise ValueError(f'Invalid column name: {column}')
        except ValueError:
            raise ValueError(f'Invalid value: {value}')
