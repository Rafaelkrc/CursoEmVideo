while True:
    n = int(input('Que ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' * 40)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 40)
print('Tabuada encerrada volte sempre!')