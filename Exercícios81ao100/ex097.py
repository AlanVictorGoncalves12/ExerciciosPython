def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    #print(f'{msg:^{tam}}') # Minha linha de código
    print('~'* tam)

# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')