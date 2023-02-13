from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
# O metodo do Curso em Vídeo
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
# Meu metodo de achar o menor e maior
"""for cont in range(0, len(numeros)):
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')"""