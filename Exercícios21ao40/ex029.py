velocidade = float(input('Qual é a velocidade atual do carro? '))

#multa2 = 80 * 2 + vel # A formula que eu criei

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')