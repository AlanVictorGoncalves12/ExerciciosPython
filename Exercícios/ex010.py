real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.06
euro = real / 5.27
iene = real / 0.039
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('E com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))
print('E com R${:.3f} você pode comprar ¥{:.3f}'.format(real, iene))