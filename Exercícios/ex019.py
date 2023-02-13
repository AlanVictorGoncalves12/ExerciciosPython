import random
from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

#Programa mostrado na aula
lista = [n1, n2, n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#Programa que eu criei
"""
for c in range(0, 10):
    num = random.randint(1, 4)
    if num == 1:
        nome = n1
    if num == 2:
        nome = n2
    if num == 3:
        nome = n3
    if num == 4:
        nome = n4
    print('O aluno escolhido foi {}'.format(nome))
    print(num)"""