# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 02:30:48 2022

@author: Tamer_S
"""
from itemSuperClass import Item
### Child Class inheriting from Parent class ITEM
class Phone(Item):
    pay_rate = 0.5
    #here we initialize the child class, with the additional attr
    def __init__(self, name:str, price:float or int, quantity:int, broken_phones:int = 0):
        #here we inherit all the attributes of the parent Class Item and all their assertions as well, although we are not mentioning the Class attributes, "all" and 'pay_rate', they are implicitly included as well since we brough the whole class with super()
        super().__init__(name, price, quantity)
        assert broken_phones >= 0 and type(broken_phones) is int, f"Enter non-negative whole number for broken phone, you entered {broken_phones}"
        self.broken_phones = broken_phones
