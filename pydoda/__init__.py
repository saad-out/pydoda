#!/usr/bin/env python3
"""
pydoda: A wrapper python library for the Darija Open Dataset

This module provides the core functionality of the pydoda library, including the main `Pydoda` class,
`Category` class for working with pre-defined categories, and `CustomCategory` class for creating custom
categories.

Classes:
    Pydoda: Main class for dataset info.
    Category: Class for working with pre-defined categories.
    CustomCategory: Class for creating custom categories.

"""

from .py_doda import Pydoda
from .category import Category
from .custom_category import CustomCategory

__all__ = ['Pydoda', 'Category', 'CustomCategory']

__version__ = '1.0.0'

def get_version() -> str:
    """Return the version of the pydoda library."""
    return __version__
