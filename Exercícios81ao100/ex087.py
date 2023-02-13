spar = scol = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] : '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            spar = spar + matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
for l in range(0, 3):
    scol = scol + matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0, 3):
    if l == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')