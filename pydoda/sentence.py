#!/usr/bin/env python3
import os

from .loader import Loader
from .utils import DATASET_DIR


class Sentence:
    """
    The Sentence class represents a specific sentence in the Doda dataset.

    It provides methods to access and retrieve information from the sentence, such as the number of entries,
    available spellings, English and Darija word translations, and Darija word variations.
    """
    def __init__(self) -> None:
        self.__dataset = DATASET_DIR
        self.__type = self.__category = 'sentences'
        try:
            self.__loader = Loader(self.__dataset, 'sentences.csv')
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
        return {'rows': shape[0], 'columns': shape[1]}
    
    def get_english_sentences(self) -> list[str]:
        """
        Returns a list of all English sentences in the category.

        Returns:
            A list of all English sentences in the category.
        """
        return self.__loader.get_column('english')
    
    def get_darija_sentences(self) -> list[str]:
        """
        Returns a list of all Darija sentences in the category.

        Returns:
            A list of all Darija sentences in the category.
        """
        return self.__loader.get_column('darija')
    
    def get_darija_translation(self, sentence: str) -> str:
        """
        Returns the Darija translation of the given English sentence.

        Args:
            sentence: The English sentence to translate.

        Returns:
            The Darija translation of the given English sentence.
        """
        try:
            return self.__loader.get_word('english', sentence, 'darija')
        except ValueError:
            return None
    
    def get_english_translation(self, sentence: str) -> str:
        """
        Returns the English translation of the given Darija sentence.

        Args:
            sentence: The Darija sentence to translate.

        Returns:
            The English translation of the given Darija sentence.
        """
        try:
            return self.__loader.get_word('darija', sentence, 'english')
        except ValueError:
            return None

    def get_translation_by_substring(self, substring: str, language: str) -> list[dict[str, str]]:
        """
        Returns a list of translations that contain the given substring.

        Args:
            substring: The substring to search for.
            language: The language of the substring.

        Returns:
            A list of translations that contain the given substring.
        """
        try:
            return self.__loader.filter_rows_by_string(language, substring)
        except KeyError:
            raise ValueError(f'Invalid language: {language}, try "english" or "darija"')
        except ValueError:
            return None