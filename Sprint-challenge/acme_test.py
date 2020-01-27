#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod2 = Product('Test Product 2')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        prod3 = Product('Test Product 3')
        self.assertEqual(prod.flammability, 0.5)

    def test_explode(self):
        prod4 = Product('Test Product 4')
        prod4.explode
        self.assert(prod4.explode = '...fizzle.')    

                 


if __name__ == '__main__':
    unittest.main()