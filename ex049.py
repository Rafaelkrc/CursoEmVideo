n = int(input('Digite um numero: '))
print('A tabuada de {} é:'.format(n))
for c in range(1, 11):
    print(n, 'x', c, '=', c * n)
