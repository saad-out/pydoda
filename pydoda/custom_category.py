#!/usr/bin/env python3
import os

from loader import Loader
from utils import CUSTOM_CATEGORIES, DATASET_DIR


class CustomCategory:
    def __init__(self, type, category) -> None:
        self.__dataset = DATASET_DIR
        if type not in ['semantic', 'syntactic', 'x-tra']:
            raise ValueError(f'Invalid category type: {type}')
        else:
            self.__type = type
        if category not in CUSTOM_CATEGORIES:
            raise ValueError(f'Invalid CustomCategory: {category}, try Category class instead')
        type_dir = self.type + ' categories' if self.type in ['semantic', 'syntactic'] else self.type
        if (category + '.csv') not in os.listdir(f'{self.__dataset}/{type_dir}'):
            raise ValueError(f'Invalid {self.type} category: {category}')
        else:
            self.__category = category
        try:
            self.__loader = Loader(self.__dataset, f'{type_dir}/{category}.csv')
        except ValueError:
            raise ValueError('Error loading category file')

    @property
    def type(self) -> str:
        return self.__type

    @property
    def category(self) -> str:
        return self.__category
    
    def entries(self) -> dict[str, int]:
        shape = self.__loader.get_shape()
        return {
            'rows': shape[0],
            'columns': shape[1]
        }
    
    def get_all_columns(self) -> list[str]:
        return self.__loader.columns

    def get_column(self, column: str) -> list:
        try:
            return self.__loader.get_column(column)
        except ValueError:
            raise ValueError(f'Invalid column: {column}')
    
    def get_row(self, column: str, value: str) -> dict[str, str]:
        try:
            return self.__loader.get_row(column=column, value=value)
        except ValueError:
            raise ValueError(f'Invalid column: {column}')
    
    def get_column_for_row(self, column: str, value: str, return_column: str) -> str:
        try:
            return self.__loader.get_word(column=column, value=value, return_column=return_column)
        except ValueError:
            raise ValueError(f'Invalid columns')