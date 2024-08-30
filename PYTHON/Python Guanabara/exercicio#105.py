#funçaõ retornando dicionario
def notas(*n, sit=False):
    """funcao para analisar notas e situações de vários alunos

    Args:
        sit (bool, optional): valor opcional, que indica a situação da turma

    Returns:
        _retorna um dicionario com varias informaçoes sobre a situação da turma"
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/ len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


#programa principal
resp = notas(5.5, 5.3, 9.5, 8, 7.3, sit=True)
print(resp)
help(notas)

