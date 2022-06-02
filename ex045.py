from random import randint
from time import sleep
item = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''Sua opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
joga = int(input('Qual é a sua jogada? '))
print('JO..')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
print('-='*12)
print('Computador jogou {}'.format(item[comp]))
print('Jogador jogou {}'.format(item[joga]))
print('-='*12)
if comp == 0:
    if joga == 0:
        print('EMPATE')
    elif joga == 1:
        print('JOGADOR VENCEU')
    elif joga == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA!')
elif comp == 1:
    if joga == 1:
        print('EMPATOU')
    elif joga == 2:
        print('JOGADOR VENCEU')
    elif joga == 0:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif comp == 2:
    if joga == 0:
        print('JOGADOR VENCEU')
    elif joga == 1:
        print('COMPUTADOR VENCEU')
    elif joga == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVALIDA')
