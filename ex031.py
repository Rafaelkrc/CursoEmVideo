d =float(input('Digite a distancia da sua viagem: '))
if d <= 200:
    print('O valor da viagem vai custar: R${:.2f}'.format(d * 0.50))
else:
    print('O valor da viagem vai custar: R${:.2f}'.format(d * 0.45))
