numero = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    while n < 0 or n > 20:
        n = int(input('Digite novamente entre 0 e 20: '))
    print(f'Voce digitou o numero {numero[n]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Programa Encerrado. Obrigado!!')
