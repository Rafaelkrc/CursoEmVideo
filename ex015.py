d = int(input('Por quantos dias alugou o carro? '))
km = float(input('Quantos km foi rodado? '))
pago = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
