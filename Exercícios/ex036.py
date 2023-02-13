valcasa = int(input('Digite o valor da casa: '))
valsalario = int(input('Digite o valor do salario: '))

valsalano = valsalario * 12
a = 1

for c in range(0, a+1):
    if valsalano <= valcasa:
        print('Valor salario por ano é {}'.format(valsalano))
        valsalano = valsalano + valsalario * 12
        a = a + 1

print('É preciso {} anos para pagar a casa'.format(a))

print('Valor salario por ano final é de {}'.format(valsalano))