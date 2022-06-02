v = float(input('Informe a velocidade do veiculo: '))
if v > 80:
    print('Voce foi multado')
    m = (v - 80) * 7
    print('A multa vai custar {:.2f} reais'.format(m))
