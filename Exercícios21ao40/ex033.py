a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Programa que eu criei
"""
if a > b > c:
    menor = c
    maior = a
if a > c > b:
    menor = b
    maior = a
if b > a > c:
    menor = c
    maior = b
if b > c > a:
    menor = a
    maior = b
if c > a > b:
    menor = b
    maior = c
if c > b > a:
    menor = a
    maior = c
"""

# Programa do vídeo
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
