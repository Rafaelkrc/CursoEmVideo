'''from calendar import isleap
ano = int(input('Informe o ano: '))
if isleap(ano):
    print('é bissexto')
else:
    print('Nao é bissesto')'''
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} nao é BISSEXTO'.format(ano))