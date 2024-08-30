def fatorial(n, mostrar=False):
    """-> calcula o fatorial de um numero:

    Args:
        n (inteiro): o numero a ser calculado;
        mostrar (bool, optional): mostar ou nao a conta;

    Returns:
       O valor fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if mostrar:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(fatorial(5, mostrar=True))