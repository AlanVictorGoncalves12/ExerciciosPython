dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = dias * 60 + (km * 15/100)
print('O total a pagar é de R${:.2f}'.format(pago))