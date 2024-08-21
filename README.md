# <p align="center">PyDODa: A Wrapper Python Library for The Darija Open Dataset</p>

<p align="center">
  <img src="https://github.com/saad-out/pydoda/blob/main/docs/images/pydoda_logo-removebg-preview.png" style="width:500px;"/>
</p>

**"This software includes data sourced from Darija Open Dataset." [GitHub](https://github.com/darija-open-dataset/dataset)**

# What is DODa ?
From the [DODa's Official GitHub repository](https://github.com/darija-open-dataset/dataset) :
> Darija Open Dataset (DODa) is an open-source project for the Moroccan dialect. With more than 21,000 entries DODa is arguably the largest open-source collaborative project for Darija <=> English translation built for Natural Language Processing purposes.
>

# What is PyDODa ?
Pydoda is a comprehensive Python library that serves as a convenient wrapper for the DODa dataset, offering seamless access and powerful analysis capabilities. The DODa dataset is a valuable linguistic resource that contains various categories of words, phrases, and sentences in Darija (Moroccan Arabic).

Pydoda simplifies the process of working with the DODa dataset, allowing researchers, developers, and language enthusiasts to explore and leverage the rich linguistic content it offers. The library provides an intuitive and efficient interface to access different categories within the dataset, retrieve spellings, translations, and perform various analyses.

By integrating Pydoda into your Python workflow, you gain access to a wide range of functionalities to extract insights from the DODa dataset. Whether you need to analyze specific semantic or syntactic categories, retrieve translations, explore variations in spellings, or investigate linguistic patterns, Pydoda empowers you to unlock the potential of the DODa dataset in an effortless manner.

# Installation
Pydoda can be easily installed using `pip`, the Python package manager:
```
$ pip3 install pydoda
```

# How It Works
Pydoda provides a simple and intuitive way to access the linguistic content of the DODa dataset. You can use the `Pydoda` class to retrieve various categories and information from the dataset.

Here's an example of how to use `Pydoda`:
```python
from pydoda import Pydoda

# Create an instance of Pydoda
pydoda = Pydoda()

# Retrieve all available categories
categories = pydoda.all()

# Print the categories in a user-friendly format
for category_type, category_list in categories.items():
    print(f"{category_type.capitalize()} Categories:")
    for category in category_list:
        print(f"- {category}")
    print()
```
Output:
```
Semantic Categories:
- malenames
- emotions
- clothes
- environment
- education
- food
- numbers
- family
- sport
- economy
- time
- femalenames
- animals
- art
- colors
- health
- humanbody
- professions
- places
- plants
- religion

Syntactic Categories:
- verbs
- adverbs
- verb-to-noun
- pronouns
- prepositions
- conjug_past
- masculine_feminine_plural
- adjectives
- conjug_present
- nouns
- imperatives
- (in)definite

X-tra Categories:
- idioms
- weird
- proverbs
- utils
- shorts

Sentences Categories:
- sentences

# etc...
```

You can use the `Category` class to retrieve specific linguistic information from a chosen category.

Here's an example of how to use `Category`:
```python
from pydoda import Category

# Create an instance of Category
my_category = Category('semantic', 'animals')

# Get the Darija translation of a word
darija_translation = my_category.get_darija_translation('dog')
print(darija_translation)
# Output: klb

# Get the English translation of a word
english_translation = my_category.get_english_translation('mch')
print(english_translation)
# Output: 'cat'
```

# Documentation
For a detailed documentation on the Pydoda library, please refer to the [official Pydoda documentation](https://saad-out.github.io/pydoda/).

# Clone Repository
To clone the Pydoda repository, use the following command:
```
git clone https://github.com/saad-out/pydoda.git --recurse-submodule
```
The `--recurse-submodule` flag is used to ensure that you also clone the submodules associated with the repository. In this case, the Pydoda library has a submodule named dataset (The Darija Open Dataset), which contains the linguistic dataset used by Pydoda. Cloning the repository with the `--recurse-submodule` flag ensures that you have access to both the Pydoda library code and the necessary dataset.

# License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The *Pydoda Library* is released under the MIT License. This license allows you to use, modify, and distribute the code for both commercial and non-commercial purposes. It grants you the freedom to adapt the library to your specific needs while providing the flexibility to incorporate it into your projects without restrictions.

For more details, please refer to the LICENSE file in the repository.
