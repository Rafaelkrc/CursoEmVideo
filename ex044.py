valor = float(input('Valor da compra:R$ '))
print('''SELECIONE A FORMA DE PAGAMENTO
[ 1 ] A vista dinheiro/cheque
[ 2 ] A vista no cartao
[ 3 ] em ate 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opcao = int(input('Forma de pagamento: '))
if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com o desconto.'.format(valor, valor - (valor * 0.1)))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} com o desconto.'.format(valor, valor - (valor * 0.05)))
elif opcao == 3:
    print('Sua compra é de R${:.2f} em 2x no cartao'.format(valor))
if opcao == 4:
    parc = int(input('Numero de parcelas: '))
    print('Sua compra sera parcelada em {}x de {:.2f} COM JUROS'.format(parc, (valor * 1.2) / parc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor * 1.2))
else:
    print('Opcao Invalida')
