from random import randint
from time import sleep


computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))

#####Programa de sorteio de azar
"""
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 1. Tente adivinhar...')
print('-=-' * 18)

for c in range(0, 5):

    n = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    r = randint(0, 1)

    while n == r:
        r = randint(0, 1)

    print('GANHEI! Eu pensei no número {} e não {}!'.format(r, n))
"""