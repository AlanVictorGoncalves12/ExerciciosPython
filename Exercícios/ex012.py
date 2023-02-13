preco = float(input('Qual é o preço do produto? R$'))
#Minha formula:
novo = preco - (preco * 0.05)
#Formula do curso
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))