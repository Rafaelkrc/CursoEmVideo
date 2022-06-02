nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('primeiro = {}'.format(lista[0]))
print('ultimo = {}'.format(lista[len(lista)-1]))