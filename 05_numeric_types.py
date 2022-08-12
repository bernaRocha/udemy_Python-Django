from decimal import *

a = Decimal('.1')
b = Decimal('.3')

x = a + a + a - b

print('x is {}'.format(x))
print(type(x))