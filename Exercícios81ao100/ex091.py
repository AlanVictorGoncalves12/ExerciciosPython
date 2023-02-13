from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
"""
#jogo = {}
for c in range(1, 5):
    jogo[f'jogadores{c}'] = f'jogador{c}'
    jogo[f'dado{c}'] = randint(1, 6)
    print(jogo[f'jogadores{c}'], end='')
    print(f' tirou {jogo[f"dado{c}"]} no dado.')
print('-=' * 30)
print(f'{"  == RANKING DOS JOGADORES =="}')
for c in range(1, 5):
    print(jogo[f'jogadores{c}'], 'com', end=' ')
    print(f'{jogo[f"dado{c}"]}.')
    #print(f'{c}º lugar: {k} com {v}.')
#print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')"""