nome = str(input('Digite seu nome completo: '))
print('Muito prazer em te conhecer!')

#Programa que eu criei
separa = nome.split()
print('Seu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[-1]))

print()
#Programa do vídeo
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
