from random import randint
numeros = (randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6), randint(0, 6))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

