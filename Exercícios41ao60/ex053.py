frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# Solução sem FOR
inverso = junto[::-1]
# Solução com FOR
"""inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]"""
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
