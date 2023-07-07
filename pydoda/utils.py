#!/usr/bin/env python3
import os


PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(PACKAGE_DIR, "dataset")


CUSTOM_CATEGORIES = [
    'malenames',
    'femalenames',
    '(in)definite',
    'conjug_past',
    'conjug_present',
    'imperatives',
    'masculine_feminine_plural',
    'verb_to_noun',
    'idioms',
    'proverbs',
]