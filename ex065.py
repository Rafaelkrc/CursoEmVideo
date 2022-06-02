resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Voce digitou {} numeros e a méedia foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
