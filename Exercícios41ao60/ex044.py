#print('=' * 12,' LOJAS ALAN ', '=' * 12)
print('{:=^40}'.format(' LOJAS ALAN '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é sua opção? '))
if opcao == 1:
    total = preco - preco * 10 / 100
elif opcao == 2:
    total = preco - preco * 5 / 100
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    totparc = int(input('Quantas parcelas? '))
    total = preco + preco * 20/100
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de {} COM JUROS.'.format(totparc, parcela))
else:
    print('Não existe essa opção. Tente novamente!')
print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(preco, total))