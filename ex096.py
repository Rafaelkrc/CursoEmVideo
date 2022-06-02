def area(larg, comp):
    a = l * c
    print(f'A Area de um terreno {larg}x{comp} é de {a}m2.')


print(' Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (mt): '))
c = float(input('Comprimento (mt): '))
area(l, c)
