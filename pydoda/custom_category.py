#!/usr/bin/env python3
import os

from .loader import Loader
from .utils import CUSTOM_CATEGORIES, DATASET_DIR


class CustomCategory:
    """
    The CustomCategory class represents a custom category in the Doda dataset.

    It provides methods to access and retrieve information from the custom category, such as the number of entries,
    available columns, retrieving a specific column, retrieving a specific row, and getting a value from a row.
    """
    def __init__(self, type, category) -> None:
        self.__dataset = DATASET_DIR
        if type not in ['semantic', 'syntactic', 'x-tra', 'ongoing']:
            raise ValueError(f'Invalid category type: {type}')
        else:
            self.__type = type
        if type != 'ongoing' and category not in CUSTOM_CATEGORIES:
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
        """
        Returns the type of the category.
        
        Returns:
            The type of the category.
        """
        return self.__type

    @property
    def category(self) -> str:
        """
        Returns the name of the category.

        Returns:
            The name of the category.
        """
        return self.__category
    
    def entries(self) -> dict[str, int]:
        """
        Returns the number of entries in the category.
        
        Returns:
            A dictionary containing the number of entries in the category.
        """
        shape = self.__loader.get_shape()
        return {
            'rows': shape[0],
            'columns': shape[1]
        }
    
    def get_all_columns(self) -> list[str]:
        """
        Returns a list of available columns in the category.
        
        Returns:
            A list of available columns in the category.
        """
        return self.__loader.columns

    def get_column(self, column: str) -> list:
        """
        Returns a list of values in the specified column.
        
        Args:
            column: The name of the column to retrieve.
        
        Returns:
            A list of values in the specified column.
        """
        try:
            return self.__loader.get_column(column)
        except ValueError:
            raise ValueError(f'Invalid column: {column}')
    
    def get_row(self, column: str, value: str) -> dict[str, str]:
        """
        Returns a dictionary containing the values of the specified row.

        Args:
            column: The name of the column to search in.
            value: The value to search for.
        
        Returns:
            A dictionary containing the values of the specified row.
        """
        try:
            return self.__loader.get_row(column=column, value=value)
        except ValueError:
            raise ValueError(f'Invalid column: {column}')
    
    def get_column_for_row(self, column: str, value: str, return_column: str) -> str:
        """
        Returns the value of the specified column for the specified row.
        
        Args:
            column: The name of the column to search in.
            value: The value to search for.
            return_column: The name of the column to return the value from.
            
        Returns:
            The value of the specified column for the specified row.
        """
        try:
            return self.__loader.get_word(column=column, value=value, return_column=return_column)
        except ValueError:
            raise ValueError(f'Invalid columns')
