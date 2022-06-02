pro = float(input('Preço do produto: '))
des = pro * 0.05
new = pro - des
print('O preço do produto é R${:.2f} \n com desconto de 5% fica no valor de:R${:.2f}'.format(pro, new))