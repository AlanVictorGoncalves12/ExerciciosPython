num = list()
pares = list()
impares = list()
c = 0
while True:
    num.append(int(input('Digite um valor: ')))
    resp = ' '
    # Meu código
    '''if num[c] % 2 == 0:
        pares.append(num[c])
    else:
        impares.append(num[c])
    c += 1'''
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
# Código do Curso em Vídeo
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
#
print('=-' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')