#Programa que eu criei
frase = str(input('Digite uma frase: ')).strip()

quant = frase.upper().count('A')
pri = frase.upper().find('A')
ult = frase.upper().rfind('A')

print('A letra A aparece {} vezes na frase.'.format(quant))
print('A primeira letra A apareceu na posição {}'.format(pri + 1))
print('A última letra A apareceu na posição {}'.format(ult + 1))

#Programa do vídeo
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))