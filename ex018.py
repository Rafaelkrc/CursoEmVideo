from math import radians, sin, cos, tan
a = float(input('Digite o angulo que voce quer: '))
print('O Angulo de {} tem o SENO de {:.2f}'.format(a, sin(radians(a))))
print('O Angulo de {} tem o COSSENO de {:.2f}'.format(a, cos(radians(a))))
print('O Angulo de {} tem a TANGENTE de {:.2f}'.format(a, tan(radians(a))))
