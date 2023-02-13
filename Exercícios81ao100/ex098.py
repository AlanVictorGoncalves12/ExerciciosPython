from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        print('-=' * 20)
        print('Passo 0 é invalido. Virou passo 1.')
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

#for c in range(i, f, p):
#    print(c, end=' ')
#print('FIM!')

'''
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)
for c in range(1, 11):
    print(c, end=' ')
    sleep(0.4)
print('FIM!')
print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, 0, -2):
    print(c, end=' ')
    sleep(0.4)
print('FIM!')
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for c in range(inicio, fim, passo):
    print(c, end=' ')
    sleep(0.4)
print('FIM!')'''