s = float(input('Qual seu Salario:R$ '))
if (s >= 1250):
    print('Com o aumento de 10% seu salario sera de: R${:.2f}'.format(s * 1.1))
else:
    print('Com o aumento de 15% seu salario sera de: R${:.2f}'.format(s * 1.15))
