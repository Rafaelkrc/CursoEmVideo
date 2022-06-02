casa = float(input('Valor da Casa: R$ '))
sal = float(input('Salario do comprador: R$ '))
tempo = int(input('Tempo de financiamento: '))
meses = tempo * 12
prest = casa/meses
valorsal = sal * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos '
      'a prestaçao sera de R${:.2f}.'.format(casa, tempo, prest))
if valorsal <= prest:
    print('Empréstimo \033[0;31mNEGADO\033[m')
else:
    print('Empréstimo \033[0;32mCONCEDIDO\033[m')
