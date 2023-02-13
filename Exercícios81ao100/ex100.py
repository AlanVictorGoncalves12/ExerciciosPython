from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

# Códigos que eu criei

# Esse 'somapar' deu errado
'''def somapar(* s):
    pares = []
    for c in range(0, len(s)):
        if s[c] % 2 == 0:
            pares.append(s[c])
    print(f'Somando os valores pares {s}, temos {sum(pares)}')'''

'''def sorteia():
    lista = [randint(1, 9), randint(1, 9), randint(1, 9),
             randint(1, 9), randint(1, 9)]
    print(f'Sorteado 5 valores da lista: ', end='')
    for k, i in enumerate(lista):
        sleep(0.5)
        print(f'{i} ', end='')
    print('PRONTO!')
    return lista'''

'''for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
print(f'Somando os valores pares {lista}, temos {sum(pares)}')'''

