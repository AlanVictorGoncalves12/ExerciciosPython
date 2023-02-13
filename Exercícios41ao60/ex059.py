from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior 
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
        # Minha versão
        """if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        else:
            print('Entre {} e {} o valor é igual'.format(n1, n2))"""
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')