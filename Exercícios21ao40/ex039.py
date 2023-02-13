from datetime import date
sexo = str(input('Diga qual é o seu sexo. [ M ] [ F ]: '))
if sexo.upper() == 'M':
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade < 18:
        #alistamento = nasc + 18 # Deu certo assim
        saldo = 18 - idade
        ano = atual + saldo
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        #alistamento = nasc + 18 # Deu certo assim
        saldo = idade - 18
        ano = atual - saldo
        print('Você já deveria ter se alistado há {} anos'.format(saldo))
        print('Seu alistamento foi em {}'.format(ano))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')
elif sexo.upper() == 'F':
    print('Você não precisa fazer alistamento obrigatorio.')
else:
    print('Você não informou o sexo corretamento. Utilize "M" ou "F" para informar.')