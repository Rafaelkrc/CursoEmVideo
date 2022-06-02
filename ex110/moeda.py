def aumentar(n=0, p=0, formato=False):
    res = n + (n * (p / 100))
    return res if formato is False else moeda(res)


def diminuir(n=0, p=0, formato=False):
    res = n - (n * (p / 100))
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(n, taxaa, True)}')
    print(f'Com {taxar}% de redução: {diminuir(n, taxaa, True)}')
    print('-' * 30)
