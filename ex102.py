def fatorial(n, show=False):
    """
    --> Calcual o Fatorial de uma numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um numero n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)