#!/usr/bin/env python3
import os
import pandas as pd
import numpy as np


class Loader:
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
        return self.__df.columns.tolist()
    
    def get_shape(self) -> tuple[int, int]:
        return self.__df.shape

    def get_column(self, column_name) -> list:
        try:
            return self.__df[column_name].tolist()
        except KeyError:
            raise ValueError(f'Invalid column name: {column_name}')
    
    def get_row(self, column, value) -> dict:
        try:
            return self.__df.loc[self.__df[column] == value].to_dict(orient='records')[0]
        except KeyError:
            raise ValueError(f'Invalid column name: {column}')
        except ValueError:
            raise ValueError(f'Invalid value: {value}')
    
    def get_word(self, column, value, return_column) -> str:
        try:
            return self.__df.loc[self.__df[column] == value, return_column].item()
        except KeyError:
            raise ValueError(f'Invalid columns')
        except ValueError:
            raise ValueError(f'Invalid value: {value}')