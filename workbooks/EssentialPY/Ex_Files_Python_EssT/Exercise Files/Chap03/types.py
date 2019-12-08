#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
from decimal import *
# x = '7.0'
# x = 7.0
# x = 7
# x = None
# x ='''
# seven

# '''

# x = 'seven {1:<9} {0:>9}'.format(8,9) #change postional argumenent  
# # x = 'seven {1:<09} {0:>09}'.format(8,9) #change postional argumenent  

# # x = 7 * 3.13453
# a = Decimal('.10')
# b = Decimal('.30')
# x = a+a+a-b
x = (1,2,3.0, ['two',4],5)
y = (1,2,3.0, ['two',4],5)
print('x is {}'.format(x))
print(type(x))
print(type(y))
print(id(x))
print(id(y))
# print(id(x[2]))

if isinstance(x,tuple):
    print("t")
elif isinstance(x,list):
    print("list")
else:
    print("Nope")