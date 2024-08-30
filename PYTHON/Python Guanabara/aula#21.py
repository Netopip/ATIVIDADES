from time import sleep
def contador(i, f, p):
    """Faz uma contagem e mostra na tela.

    Args:
       i (inicio): inicio da contagem
       f (fim): fim da contagem
       p (passo): passo da contagem
    """
    c = i
    while c<= f:
        print(f'{c} ',end='', flush=True)
        c += p
        sleep(0.5)
    print('Fim')
    
help(contador)





        