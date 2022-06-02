from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Voce tem que se alistar \033[31mimediatamente!\033[m')
elif idade < 18 and idade > 0:
    saldo = 18 - idade
    print('Voce ainda nao tem 18 anos ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 0:
    print('\033[32mA data de {} ainda nao chegou, verifique.'.format(atual))
