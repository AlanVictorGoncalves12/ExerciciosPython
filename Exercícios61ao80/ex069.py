totM20 = totH = tot18 = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    sexo = ' '
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-' * 30)
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade < 20 and sexo in 'F':
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')