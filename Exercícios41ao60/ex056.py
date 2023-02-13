somaidade = maioridadehomem = totmulher20 = 0
nomevelho = ''
for p in range(1, 5):
    print('{:-^21}'.format(' {}ª PESSOA '.format(p)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))