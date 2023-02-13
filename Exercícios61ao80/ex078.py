listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if maior < listanum[c]:
            maior = listanum[c]
        elif menor > listanum[c]:
            menor = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')