r1 = float(input('Digite o cumprimento da primeira reta: '))
r2 = float(input('Digite o cumprimento da segunda reta: '))
r3 = float(input('Digite o cumprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os seguimentos acima NAO PODEM FORMAR triangulos')