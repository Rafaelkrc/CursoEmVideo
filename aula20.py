#exercicio sem funcao
#a = 4
#b = 5
#s = a + b
#print(s)
#a = 8
#b = 9
#s = a + b
#print(s)

#a = 2
#b = 1
#s = a + b
#print(s)
############# SEMPRE DEIXAR 2 LINHAS DE ESPAçO DEPOIS DA FUNCAO DEF
print('-' * 40)
print('funcao, cria-se uma variavel que sempre que colocar ela vai gerar a rotina criada nela')
def soma(a=0, b=0):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

print('-' * 40)
print('Funcao para receber quantos numeros quiser')


def contador(* num): #com o * e o nome da variavel ele
                    #aceita quantos parametros quiser, e vai criar tuplas.
    print(num)


contador(2, 1, 7)
contador(8, 4)
contador(4, 4, 7, 6, 2)


print('-' * 40)
print('Dobrar os valores de uma lista')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

print('-' * 40)
print('desempacotamento')

def soma(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')


soma(5, 2)
soma(2, 9, 4)
