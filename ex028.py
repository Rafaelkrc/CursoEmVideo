'''from random import choice
num = int(input('Acerte o numero escolhido pelo computador: '))
lista = [1 , 2, 3, 4, 5]
escolhido = choice(lista)
print('O numero informado foi: {}'.format(num))
if num == escolhido:
    print('Voce acertou, o numero escolhido pelo computador foi {}'.format(escolhido))
else:
    print('Voce errou, tente novamente, o numero escolhido pelo computador foi {}'.format(escolhido))
print('Até a proxima!')'''

from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador escolher um numero de 0 a 5
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO')
sleep(3)
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no numero {} e nao no numero {}!'.format(computador, jogador))