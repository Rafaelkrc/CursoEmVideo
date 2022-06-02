a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
maior = a
if (b>a and b>c):
    maior = b
if (c>a and c>b):
    maior = c
menor = a
if (b<a and b<c):
    menor = b
if (c<a and c<b):
    menor = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
