# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 02:29:23 2022

@author: Tamer_S
"""

import csv
class Item:
    pay_rate = 0.8 # class gobal attr that is accesed across all items
    # This attr is called to apply 20% disc to pirce
    all = []
    def __init__(self, name: str, price: float, quantity: int = 0):

        # Run validations to the received args
        assert type(name) is str, f"object name {name} must be a string"
        assert type(price) is float or type(price) is int, f"Enter a numeric value for price {price}"
        assert type(quantity) is int, f"{quantity} must be a whole num"
        assert price and quantity >= 0, f"price {price} and quantity {quantity} can't be negative value"

        # Defining attrs
        # the left-only dunder for the name is added since we will encapsulate that attr (make it private) in the future using the property decorator, it will be read-only after instantiation of the object
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to excute
        Item.all.append(self)
    
    ## Encapsulation: Here we define the entered name as 'read-only', it won't allow any overwritting or modifications once the instance is created
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception(f"Name {value} is too long")
        else:
            self.__name = value
    
    
    
    def calculate_total_price(self):
        return (self.quantity * self.price)


    def apply_discount(self):
        self.price  *= self.pay_rate
        return(self.price)
    
    ### Dealing with database, storing in csv file, must be a class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name= item.get('name'),
                price= float(item.get('price')),
                quantity= int(item.get('quantity')))
    
    @staticmethod
    def is_integer(num):
    ### the method called .is_integer() counts out float with .0 
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            # checks if it's int
            return True
        else:
            return False
    
    ### ABSTRACTION
    def __connect(self, smtp_server):
        pass
    
    def __prepare_body(self):
        return f'Hi user, we have {self.name} with quantity {self.quantity}'
    
    def __send(self):
        pass
    
    def __send_email(self):
        self.__connect("")
        self.__prepare_body()
        self.__send()
    
    
    ### repr to print our instances as str, in the class name, we use the dunder to call the calss name genericly, just in case we created a child class, so this will inspect what class name the object is generated from and return the correct class name
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"











