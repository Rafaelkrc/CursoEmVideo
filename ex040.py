nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print('Quem tirou a nota {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))
if media < 5:
    print('O Aluno esta \033[1;31mREPROVADO!\033[m')
elif media >= 5 and media <= 6.9:
    print('O Aluno esta em \033[1;33mRECUPERACAO\033[m')
else:
    media >= 7
    print('O Aluno esta \033[1;32mAPROVADO\033[m')

