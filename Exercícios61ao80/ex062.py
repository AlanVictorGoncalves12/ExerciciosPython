print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
# Versão do Curso em Vídeo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

# Versão minha
'''cont = cont2 = 1
fim = 10
while fim != 0:
    while cont <= fim:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
        cont2 += 1
    print('PAUSA')
    fim = int(input('Quantos termos você quer mostrar a mais? '))
    cont = 1
print('Progressão finalizada com {} termos mostrados.'.format(cont2 - 1))'''

