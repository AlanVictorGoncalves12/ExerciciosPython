salario = float(input('Qual é o salário do Funcionário? R$'))

#Outra formula:
novo = salario + (salario * 0.15)
#Formula do video
novo = salario + (salario * 15/100)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))

print('\nContinuação da aula:')
produto = float(input('Qual é o preço do produto? R$'))
desconto = produto - (produto * 10/100)
aumento = produto + (produto * 8/100)
print('O preço do produto é R${}, pagando a vista ele é R${}'.format(produto, desconto))
print('O preço do produto pagando parcelado é R${}'.format(aumento))