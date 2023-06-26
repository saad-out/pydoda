#!/usr/bin/env python3
"""
This module contains unittests for the `Pydoda` class.
"""
import unittest
import os

from pydoda import Pydoda
from pydoda.utils import CUSTOM_CATEGORIES


class TestPydoda(unittest.TestCase):
    """
    This class contains unittests for the `Pydoda` class.
    """

    maxDiff = None

    def setUp(self):
        """
        This method is run before each test.
        """
        self.pydoda = Pydoda()

    def test_get_semantic_categories(self):
        """
        This method tests the `get_semantic_categories()` method.
        """
        semantic_cats = [cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/semantic categories')]
        self.assertEqual(self.pydoda.get_semantic_categories(), semantic_cats)
    
    def test_get_syntactic_categories(self):
        """
        This method tests the `get_syntactic_categories()` method.
        """
        syntactic_cats = [cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/syntactic categories')]
        self.assertEqual(self.pydoda.get_syntactic_categories(), syntactic_cats)
    
    def test_get_xtra(self):
        """
        This method tests the `get_xtra()` method.
        """
        xtra_cats = [cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/x-tra')]
        self.assertEqual(self.pydoda.get_xtra(), xtra_cats)
    
    def test_all(self):
        """
        This method tests the `all()` method.
        """
        all_cats = {
            'semantic': [cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/semantic categories')],
            'syntactic': [cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/syntactic categories')],
            'x-tra': [cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/x-tra')],
            'sentences': ['sentences']
        }
        self.assertEqual(self.pydoda.all(), all_cats)
    
    def test_classes(self):
        """
        This method tests the `classes()` method.
        """
        all = [cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/semantic categories')]
        all.extend([cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/syntactic categories')])
        all.extend([cat.replace('.csv', '') for cat in os.listdir('pydoda/dataset/x-tra')])
        classes = {
            'Category': [cat for cat in all if cat not in CUSTOM_CATEGORIES],
            'CustomCategory': CUSTOM_CATEGORIES,
            'Sentence': ['sentences']
        }
        self.assertEqual(self.pydoda.classes(), classes)
