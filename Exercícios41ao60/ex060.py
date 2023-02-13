# Modo de fazer fatorial usando modulo
'''from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

# Outro modo de fazer Fatorial
'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''

# O código que eu tentei fazer
num = int(input('Digite um número para calcular seu Fatorial: '))
print('Calculando {}! ='.format(num), end='')
num2 = num
cont = 0
f = 1
for c in range(num, 0, -1):
    f = f * c
    if c != num2:
        print('x', end='')
    print(' {} '.format(c), end='')
print('= {}'.format(f))