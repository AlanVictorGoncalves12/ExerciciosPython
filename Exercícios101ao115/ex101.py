def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa principal
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

# Programa que eu criei
'''def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    return idade

print('-' * 30)
ano = int(input('Em que ano você nasceu? '))

print(f'Com {voto(ano)} anos: ', end='')
if voto(ano) < 16:
    print('NÃO VOTA.')
elif voto(ano) < 18:
    print('VOTO OPCIONAL.')
elif voto(ano) < 60:
    print('VOTO OBRIGATORIO.')
else:
    print('VOTO OPCIONAL.')'''