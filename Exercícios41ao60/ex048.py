soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        #print(c, end=' ')
        cont += 1   #Que é a mesma coisa que: cont = cont + 1
        soma += c   #Que é a mesma coisa que: soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))