from random import randint
print('=' * 40)
print('VAMOS JOGAR PAR OU IMPAR')
v = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu!')
            v += 1
        else:
            print('Voce Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce Venceu')
            v += 1
        else:
            print('Voce Perdeu!')
            break
    print('Vamos Jogar novamente...')
print(f'GAME OVER!!! Voce venceu {v} vezes')
