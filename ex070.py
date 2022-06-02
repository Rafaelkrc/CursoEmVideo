pro = soma = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Informe o preço do produto: R$ '))
    soma += preco
    cont += 1
    if preco > 1000:
        pro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R${soma:.2f}')
print(f'Tem {pro} produtos com preço maior que R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

