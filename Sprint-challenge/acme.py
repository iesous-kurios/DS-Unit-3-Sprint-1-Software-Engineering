"""Software Engineering - the Acme Way"""

import numpy as np

class Product:
    """Base class for all Products.
    :var name: str
    :var price: int
    :var weight: int
    :var flammability: float
    :var identifier: rand.int

    Methods:
    - stealability(self)
        - calculates the price divided by the weight, 
        and then returns a message: 
        if the ratio is less than 0.5 return "Not so stealable...", 
        if it is greater or equal to 0.5 but less than 1.0 return "Kinda stealable.", 
        and otherwise return "Very stealable!"
        
    - explode(self) - calculates the flammability times the weight, 
    and then returns a message: if the product is less than 10 return "...fizzle.", 
    if it is greater or equal to 10 but less than 50 return "...boom!", 
    and otherwise return "...BABOOM!!"

    """

    def __init__(self, name: str) -> None:
        # Instance variable.
        self.name = None
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = np.random.randint(1000000, 10000000)

    def __repr__(self):
        """Return the class name and dict of instance variables and their values when printing the instance."""
        return f'{self.__class__} {self.__dict__}'

    def stealability(self) -> None:
        """calculates price divided by weight, and returns a message"""
        cop_that = self.price / self.weight
        if cop_that < 0.5:
            print('Not so stealable...')

        if cop_that >= 0.5:
            if cop_that < 1.0:
                print('Kinda stealable')

        if cop_that >= 1.0:
            print('Very stealable!')

    def explode(self) -> None:
        """calculates flammability multiplied by weight, and returns a message"""
        go_boom = self.flammability * self.weight
        if go_boom < 10:
            print('...fizzle.')

        if go_boom >= 10:
            if go_boom < 50:
                print('...boom!')

        if go_boom >= 50:
            print('...BABOOM!!')            

class BoxingGlove(Product):
    """Class for making Boxing Gloves. Inherits from Product.
    
    Class variables:
    - weight: 10
    - overrides explode function from Product class

    Methods:
    - punch:
        - checks weight then returns a message.
    
    """

    def __init__(self, name: str, ) -> None:
        # Call super to instantiate parent class instance variables.
        super().__init__(name)  # Pass parent variables to super.
        # Instantiate a specific product instance variable.
        self.weight = 10            
    
    def punch(self) -> None:
        """get weight of glove then determine if it will hurt to get punched by this particular glove"""

        if self.weight < 5:
            print('That tickles.')

        if self.weight >= 5:
            if self.weight < 15:
                print('Hey that hurt!')

        if self.weight >= 15:
            print('OUCH!')            

    def explode(self) -> None:
        print("...it's a glove")   
        




