continuacao = 's'
quant = soma = num = 0
while continuacao not in 'Nn' and continuacao in 'Ss':
    num = int(input('Digite um número: '))
    quant += 1
    soma += num
    continuacao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))