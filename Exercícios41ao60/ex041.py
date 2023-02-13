from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
"""
if idade > 25:
    print('Classificação: MASTER')
elif idade > 19:
    print('Classificação: SÊNIOR')
elif idade > 14:
    print('Classificação: JUNIOR')
elif idade > 9:
    print('Classificação: INFANTIL')
else:
    print('Classificação: MIRIM')"""

#Outra ordem do IF, apresentada no vídeo
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')