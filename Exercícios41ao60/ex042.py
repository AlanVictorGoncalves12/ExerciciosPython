r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    #elif r1 == r2 != r3 or r2 != r1 == r3 or r3 == r2 != r1: Forma possivel mas desnecessaria
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
