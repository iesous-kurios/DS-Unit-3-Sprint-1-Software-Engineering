#!/usr/bin/env python
from acme import Product
from itertools import chain
from random import randint, sample, uniform


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    i = 0
    while i < num_products:
        x = Product(object)
        x.name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        x.price = random.randint(5, 101)
        x.weight = random.randint(5, 101)
        x.flammability = random.uniform(0.0, 2.6)
        products.append(x)
        i += 1
    return products  

def inventory_report(products):
    unique_words = set(products)          
    unique_word_count = len(unique_words)
    print('Total unique name combinations is: ', unique_word_count)


    
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())    

