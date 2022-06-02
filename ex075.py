n1 = (int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o quarto valor: ')))
print(f'Voce digitou os valores {n1}')
print(f'o Numero 9 apareceu {n1.count(9)} vezes')
if 3 in n1:
    print(f'o Valor 3 apareceu na {n1.index(3)+1}° posicao')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao')
print('Os valores pares digitados foram ', end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' ')
