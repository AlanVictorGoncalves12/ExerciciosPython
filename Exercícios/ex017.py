import math
from math import hypot

co = float(input('Compimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))