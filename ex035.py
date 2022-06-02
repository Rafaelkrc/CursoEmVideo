print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)
r1 = float(input('Digite o cumprimento da primeira reta: '))
r2 = float(input('Digite o cumprimento da segunda reta: '))
r3 = float(input('Digite o cumprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triangulos')
else:
    print('Os seguimentos acima NAO PODEM FORMAR triangulos')
