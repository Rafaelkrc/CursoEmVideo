from random import randint
computador = randint(0, 10)
cont = 0
acertou = False
print('Vou pensar em um numero de 0 a 10. Tente adivinhar!')
while not acertou:
    jogador = int(input('Qual é o seu palpite: '))
    cont += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais um vez.')
        elif jogador > computador:
            print('Menos... Tente mais um vez.')
print('PARABéNS VOCE TENTOU {}X ATé ACERTAR!!!'.format(cont))