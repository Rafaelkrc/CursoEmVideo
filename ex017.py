import math
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))


'''co = float(input('Informe o cateto oposto: '))
ca = float(input('Informa o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
