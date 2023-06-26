#!/usr/bin/env python3
import os

from .loader import Loader
from .utils import CUSTOM_CATEGORIES, DATASET_DIR


class Category:
    """
    The Category class represents a specific category in the Doda dataset.

    It provides methods to access and retrieve information from the category, such as the number of entries,
    available spellings, English and Darija word translations, and Darija word variations.
    """
    def __init__(self, type, category) -> None:
        self.__dataset = DATASET_DIR
        if type not in ['semantic', 'syntactic', 'x-tra']:
            raise ValueError(f'Invalid category type: {type}')
        else:
            self.__type = type
        if category in CUSTOM_CATEGORIES:
            raise ValueError(f'Invalid Category: {category}, try CustomCategory class instead')
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
            The number of entries in the category.
        """
        shape = self.__loader.get_shape()
        return {
            'rows': shape[0],
            'columns': shape[1]
        }
    
    def get_spellings(self) -> list[str]:
        """
        Returns a list of available spellings in the category.
        
        Returns:
            A list of available spellings in the category.
        """
        columns = self.__loader.columns
        return [column for column in columns if column != 'eng']
    
    def get_english_words(self) -> list:
        """
        Returns a list of available English words in the category.

        Returns:
            A list of available English words in the category.
        """
        return self.__loader.get_column('eng')

    def get_darija_words(self, spelling: str = 'n1') -> list:
        """
        Returns a list of available Darija words in the category.

        Args:
            spelling: The spelling to retrieve. Defaults to 'n1'.

        Returns:
            A list of available Darija words in the category.
        """
        try:
            return self.__loader.get_column(spelling)
        except ValueError:
            raise ValueError(f'Invalid spelling: {spelling}')
    
    def get_darija_translation(self, word: str, spelling: str = 'n1') -> str:
        """
        Returns the Darija translation of the specified word.

        Args:
            word: The word to retrieve.
            spelling: The spelling to retrieve. Defaults to 'n1'.
        
        Returns:
            The Darija translation of the specified word.
        """
        try:
            return self.__loader.get_word(column='eng', value=word, return_column=spelling)
        except ValueError:
            return None
    
    def get_english_translation(self, word: str, spelling: str = 'n1') -> str:
        """
        Returns the English translation of the specified word.
        
        Args:
            word: The word to retrieve.
            spelling: The spelling to retrieve. Defaults to 'n1'.
            
        Returns:
            The English translation of the specified word.
        """
        try:
            return self.__loader.get_word(column=spelling, value=word, return_column='eng')
        except ValueError:
            return None
    
    def get_darija_variations(self, word: str) -> dict[str, str]:
        """
        Returns a dictionary containing the Darija variations of the specified word.
        
        Args:
            word: The word to retrieve.
        
        Returns:
            A dictionary containing the Darija variations of the specified word.
        """
        try:
            row = self.__loader.get_row(column='eng', value=word)
            if 'eng' in row: del row['eng']
            return row
        except ValueError:
            return None
