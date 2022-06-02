from datetime import date
atual = date.today().year
ano = int(input('Informe o ano de nascimento: '))
idade = atual - ano
print('voce tem {} anos'.format(idade))
if idade <= 9:
    print('Sua categoria vai ser \033[34mMIRIM\033[m!')
elif idade > 9 and idade <= 14:
    print('Sua categoria vai \033[34mINFANTIL\033[m!')
elif idade > 14 and idade <=19:
    print('Sua catgoria vai ser \033[34mJUNIOR\033[m!')
elif idade > 19 and idade <= 25:
    print('Sua categoria vai ser \033[34mSENIOR\033[m!')
elif idade > 25:
    print('Sua categoria vai ser \033[34mMASTER\033[m!')