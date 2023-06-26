#!/usr/bin/env python3
import os

from .utils import DATASET_DIR


class Pydoda:
    """
    The Pydoda class provides methods to access and work with Doda datasets.

    This class allows you to retrieve and explore different categories of Doda datasets, such as semantic categories, syntactic categories,
    and additional extra categories. It also provides a method to retrieve all available categories.

    Methods:
        get_semantic_categories(): Returns a list of available semantic categories.
        get_syntactic_categories(): Returns a list of available syntactic categories.
        get_xtra(): Returns a list of available extra categories.
        all(): Returns a dictionary containing all available categories.

    Example usage:
        pydoda = Pydoda()
        semantic_cats = pydoda.get_semantic_categories()
        print(semantic_cats)  # ['category1', 'category2', ...]

    """
    def __init__(self) -> None:
        self.__dataset = DATASET_DIR

    def get_semantic_categories(self) -> list[str]:
        """
        Returns a list of available semantic categories.
        
        Returns:
            A list of available semantic categories.
        """
        return [category.replace('.csv', '') for category in os.listdir(f'{self.__dataset}/semantic categories')]
    
    def get_syntactic_categories(self) -> list[str]:
        """
        Returns a list of available syntactic categories.
        
        Returns:
            A list of available syntactic categories.
        """
        return [category.replace('.csv', '') for category in os.listdir(f'{self.__dataset}/syntactic categories')]
    
    def get_xtra(self) -> list[str]:
        """
        Returns a list of available extra categories.
        
        Returns:
            A list of available extra categories.
        """
        return [category.replace('.csv', '') for category in os.listdir(f'{self.__dataset}/x-tra')]
    
    def all(self) -> dict[str, list[str]]:
        """
        Returns a dictionary containing all available categories.

        Returns:
            A dictionary containing all available categories.
        """
        return {
            'semantic': self.get_semantic_categories(),
            'syntactic': self.get_syntactic_categories(),
            'x-tra': self.get_xtra(),
            'sentences': ['sentences']
        }
