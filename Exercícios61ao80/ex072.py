cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'noze',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
num = 0
while True:
    if num < 0 or num > 20:
        print('Tente novamente. ', end='')
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp == 'N':
            break
print('Programa encerrado. Volte sempre!')

#Minha versão do codigo
"""num = -1
while num < 0 or num > 20:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente. ', end='')
if num == 0:
    extenso = 'zero'
elif num == 1:
    extenso = 'um'
elif num == 2:
    extenso = 'dois'
elif num == 3:
    extenso = 'três'
elif num == 4:
    extenso = 'quatro'
elif num == 5:
    extenso = 'cinco'
elif num == 6:
    extenso = 'seis'
elif num == 7:
    extenso = 'sete'
elif num == 8:
    extenso = 'oito'
elif num == 9:
    extenso = 'nove'
elif num == 10:
    extenso = 'dez'
elif num == 11:
    extenso = 'onze'
elif num == 12:
    extenso = 'doze'
elif num == 13:
    extenso = 'treze'
elif num == 14:
    extenso = 'quatorze'
elif num == 15:
    extenso = 'quinze'
elif num == 16:
    extenso = 'desseseis'
elif num == 17:
    extenso = 'dessesete'
elif num == 18:
    extenso = 'dezoito'
elif num == 19:
    extenso = 'dezenove'
elif num == 20:
    extenso = 'vinte'
print(f'Você digitou o número {extenso}')"""