print('-=' * 50)
print('docinstrings')

def contador(i, f, p):
    """
    --> Faz uma contagem e mostra na tela
    :param i: inicio da ocntagem
    :param f: fim da contagem
    :param p: passo da contagem, de quanto em quanto vai pular
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)

#####################
print('-=' * 50)
print('PARAMETROS CONDICIONAIS')


def somar(a=0, b=0, c=0):
    """
    -->> Faz a soma de tres valores e mostra o resultado
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    é adicionado o zero a cada variavel, pois se nao foi
    informado nenhum valor, a funçao ira adicionar o zero
    para completar o calculo
    """
    s = a + b + c
    print((f'A soma vale {s}.'))


somar(3, 2, 5)
somar(8, 4)

print('-=' * 50)
print('ESCOPO DE VARIAVEIS')


def funcao():
    """
    as variaveis declaradas dentro do def, so valeram dentro do def.
    e a variaveis declaradas fora do def, ou seja, no programa principal
    valeram e fora do def, ou seja, no programa prinicipal e poderao
    valer dentro do def, caso no def nao tenha uma variavel com o mesmo
    nome.
    mas se eu colocar a palavra Global e o nome da variavel, por exemplo:
    global n1, a variavel n1 que esta fora, vai perder o seu valor e vai
    assumir o valor da variavel n1 que esta dentro do def.
    """
    n1 = 4
    print(f'N1 dentro vale {n1}')


#Programa principal
n1 = 2
funcao()
print(f'N1 fora vale {n1}')


print('-=' * 50)
print('RETORNO DE VALORES')


def somar(a=0, b=0, c=0):
    """
    com a funçao return eu informo a variavel do resultado que quero,
    crio outras variaveis para a varial principal, no caso somar, e o print
    retorna conforme a formataçao que quero.
    """
    s = a + b + c
    print(f'A soma vale {s}')
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')




print('-=' * 50)
print('EXERCICIO')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'O resultados sao {f1}, {f2} e {f3}')

print('-=' * 50)
print('EXERCICIO')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
print(par(num))
if par(num):
    print('E par!')
else:
    print('E impar!')
