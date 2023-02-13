#Programa que eu criei
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? ', end=' ')
print(nome[(nome.lower().find('silva')):(nome.lower().find('silva') + 5)].lower() == 'silva')

#Programa do vídeo
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))