#!/usr/bin/env python3
"""
This module contains unittests for the `Category` class.
"""
import unittest
import random
import os
import pandas as pd
import numpy as np

from pydoda import Pydoda, Category
from pydoda.utils import DATASET_DIR, CUSTOM_CATEGORIES


class TestCategory(unittest.TestCase):
    """
    This class contains unittests for the `Category` class.
    """

    maxDiff = None
    categories = Pydoda().classes()['Category']
    types = ['semantic', 'syntactic', 'x-tra']

    def setUp(self):
        """
        This method is run before each test.
        """
        self.type = random.choice(self.types)
        type_categories = Pydoda().all()[self.type]
        category_name = random.choice(self.categories)
        while category_name not in type_categories:
            category_name = random.choice(self.categories)
        self.category = category_name
        self.cat = Category(self.type, self.category)
        self.path = f'{DATASET_DIR}/'
        if self.type in ['semantic', 'syntactic']:
            self.path += f'{self.type} categories/'
        else:
            self.path += f'{self.type}/'
        self.df = pd.read_csv(f'{self.path}{self.category}.csv')
        self.df = self.df.replace(np.nan, None)
        print(f'\nRunning test for {self.type} category: {self.category} in path: {self.path}\n')


    def test_instantiation(self):
        """
        This method tests the instantiation of the `Category` class.
        """
        with self.assertRaises(ValueError):
            Category('invalid type', random.choice(self.categories))
        with self.assertRaises(ValueError):
            Category(random.choice(self.types), 'invalid category')
        with self.assertRaises(ValueError):
            Category(random.choice(self.types), random.choice(CUSTOM_CATEGORIES))
    
    def test_type(self):
        """
        This method tests the `type` property of the `Category` class.
        """
        self.assertEqual(self.cat.type, self.type)
    
    def test_category(self):
        """
        This method tests the `category` property of the `Category` class.
        """
        self.assertEqual(self.cat.category, self.category)
    
    def test_entries(self):
        """
        This method tests the `entries` method of the `Category` class.
        """
        shape = self.cat.entries()
        self.assertIsInstance(shape, dict)
        self.assertEqual(len(shape), 2)
        self.assertIsInstance(shape['rows'], int)
        self.assertIsInstance(shape['columns'], int)
        self.assertGreater(shape['rows'], 0)
        self.assertGreater(shape['columns'], 0)
        rows, columns = self.df.shape
        self.assertEqual(shape['rows'], rows)
        self.assertEqual(shape['columns'], columns)
    
    def test_get_spellings(self):
        """
        This method tests the `get_spellings` method of the `Category` class.
        """
        spellings = self.cat.get_spellings()
        self.assertIsInstance(spellings, list)
        self.assertGreater(len(spellings), 0)
        spellings.append('eng')
        self.assertEqual(spellings, list(self.df.columns))
    
    def test_get_english_words(self):
        """
        This method tests the `get_english_words` method of the `Category` class.
        """
        words = self.cat.get_english_words()
        self.assertIsInstance(words, list)
        self.assertGreater(len(words), 0)
        self.assertEqual(words, self.df['eng'].tolist())
    
    def test_get_darija_words(self):
        """
        This method tests the `get_darija_words` method of the `Category` class.
        """
        spellings = self.cat.get_spellings()
        for spelling in spellings:
            words = self.cat.get_darija_words(spelling)
            self.assertIsInstance(words, list)
            self.assertGreater(len(words), 0)
            self.assertEqual(words, self.df[spelling].tolist())
    
    def test_get_darija_translation(self):
        """
        This method tests the `get_darija_translation` method of the `Category` class.
        """
        word = random.choice(self.df['eng'].tolist())
        translation = self.df[self.df['eng'] == word]['n1'].tolist()[0]
        self.assertEqual(self.cat.get_darija_translation(word), translation)
    
    def test_get_english_translation(self):
        """
        This method tests the `get_english_translation` method of the `Category` class.
        """
        word = random.choice(self.df['n1'].tolist())
        translation = self.df[self.df['n1'] == word]['eng'].tolist()[0]
        self.assertEqual(self.cat.get_english_translation(word), translation)

