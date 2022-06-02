valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 ==0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os valores digitados foram {valores}')
print(f'O valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')