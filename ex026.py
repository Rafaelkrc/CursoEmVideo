frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A letra A aparece na posiçao: {}'.format(frase.find('A')+1))
print('A letra A aparece na ultima vez na posiçao: {}'.format(frase.rfind('A')+1))