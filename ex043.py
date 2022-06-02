peso = float(input('Informa seu peso em kg: '))
altura = float(input('Informe sua altura: '))
IMC = peso/(altura ** 2)
print(('O Seu IMC calculado foi de: {:.2f} '.format(IMC)))
if IMC < 18.5:
    print('Voce esta Abaixo do Peso')
elif IMC < 25:
    print('Voce esta no Peso Ideal')
elif IMC < 30:
    print('Voce esta com Sobrepeso')
elif IMC < 40:
    print('Voce esta com Obesidade')
else:
    print('Voce esta com Obesidade Morbida')
