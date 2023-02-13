"""u = d = c = m = 0
num = str(input('Informe um número: '))
if len(num) == 1:
    u = num[0]
if len(num) == 2:
    d = num[0]
    u = num[1]
if len(num) == 3:
    c = num[0]
    d = num[1]
    u = num[2]
if len(num) == 4:
    m = num[0]
    c = num[1]
    d = num[2]
    u = num[3]"""

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
