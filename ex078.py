valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {mai} nas posicoes ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digita do foi {men} nas posicoes ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}... ', end='')
print()
