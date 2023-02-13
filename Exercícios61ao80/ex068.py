from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
v = 0
while True:
    print('=-' * 20)
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = (input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-' * 40)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 40)
    # Versão do Curso em Vídeo
    if tipo == 'P':
        if total % 2 ==0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break

    # Minha versão de IF
    """if tipo == 'P' and (total) % 2 == 0:
        print('Você VENCEU!')
        v += 1
    elif tipo == 'I' and (total) % 2 == 1:
        print('Você VENCEU!')
        v += 1
    else:
        print('Você PERDEU!')
        print('=-' * 20)
        break"""

    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')

