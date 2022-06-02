from time import sleep
num0 = int(input('Digite um valor: '))
num1 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    opcao = int(input('Qual é a sua opçao: '))
    if opcao == 1:
        soma = num0 + num1
        print('A soma de {} e {} é igual a {}'.format(num0, num1, soma))
    elif opcao == 2:
        produto = num0 * num1
        print('A multiplicaçao de {} x {} é igual a {}'.format(num0, num1, produto))
    elif opcao == 3:
        if num0 > num1:
            maior = num0
        else:
            maior = num1
        print('Entre {} e {} o maior valor é {}'.format(num0, num1, maior))
    elif opcao == 4:
        print('Informe os numeros novamente:')
        num0 = int(input('Digite um valor:'))
        num1 = int(input('Digite outro valor: '))
    elif opcao ==5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')


