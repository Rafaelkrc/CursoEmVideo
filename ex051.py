term = int(input('Primeiro Termo: '))
raz = int(input('Razao: '))
decimo = term + (10 - 1) * raz
for c in range(term, decimo + raz, raz):
    print(c, end=' -> ')
print('Acabou', end='')
