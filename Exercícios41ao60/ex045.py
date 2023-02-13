from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'''.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')

"""
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)
if jogador == 0:
    escolhajog = 'Pedra'
elif jogador == 1:
    escolhajog = 'Papel'
elif jogador == 2:
    escolhajog = 'Tesoura'
else:
    print('Não existe essa escolha. Tente novamente!')
if computador == 0:
    escolhapc = 'Pedra'
elif computador == 1:
    escolhapc = 'Papel'
elif computador == 2:
    escolhapc = 'Tesoura'


sleep(0.8)
print('JO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!')
sleep(0.8)

if computador == jogador == 0:
    result = 'EMPATE'
elif computador == jogador == 1:
    result = 'EMPATE'
elif computador == jogador == 2:
    result = 'EMPATE'
elif computador == 0 and jogador == 1:
    result = 'JOGADOR VENCE'
elif computador == 1 and jogador == 0:
    result = 'COMPUTADOR VENCE'
elif computador == 1 and jogador == 2:
    result = 'JOGADOR VENCE'
elif computador == 2 and jogador == 1:
    result = 'COMPUTADOR VENCE'
elif computador == 2 and jogador == 0:
    result = 'JOGADOR VENCE'
elif computador == 0 and jogador == 2:
    result = 'COMPUTADOR VENCE'
print('-=' * 11)
print('''Computador jogou {}
Jogador jogou {}'''.format(escolhapc, escolhajog))
print('-=' * 11)
print(result)
"""