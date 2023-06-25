#!/usr/bin/env python3
import os

from utils import DATASET_DIR


class Pydoda:
    def __init__(self) -> None:
        self.__dataset = DATASET_DIR

    def get_semantic_categories(self) -> list[str]:
        return [category.replace('.csv', '') for category in os.listdir(f'{self.__dataset}/semantic categories')]
    
    def get_syntactic_categories(self) -> list[str]:
        return [category.replace('.csv', '') for category in os.listdir(f'{self.__dataset}/syntactic categories')]
    
    def get_xtra(self) -> list[str]:
        return [category.replace('.csv', '') for category in os.listdir(f'{self.__dataset}/x-tra')]
    
    def all(self) -> dict[str, list[str]]:
        return {
            'semantic': self.get_semantic_categories(),
            'syntactic': self.get_syntactic_categories(),
            'x-tra': self.get_xtra(),
            'sentences': ['sentences']
        }