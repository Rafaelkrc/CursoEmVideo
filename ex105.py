def notas(*n, sit=False):
    """
    --> Função para analizar notas e situação de vários alunos.
    :param n: uma ou mais notas dos alubos(aceita várias)
    :param sit: valor opcional, indincando se deve ou não adicionar a situção
    :return: dicionário com várias informações sobre a situação da truma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)