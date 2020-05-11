'''
A lista p representa um polinomio que tem seu quocienetes lidos começando
do fim da lista até o começo, sendo b a raiz a ser testada pelo programa.
Ex: [-2, 1, 1] representa x^2 + x - 2
'''

def polinomioComRaiz(p, b):
    x = len(p) - 1
    result = 0
    soma = 1
    o = 0
    w = 0
    while x >= 0:
        if x != 0:
            for w in range(o, len(p)-1):
                soma = soma * (p[x]*b)
            x -= 1
            o += 1
            result += soma
            soma = 1
        else:
            result += p[x]
            x -= 1
    if result == 0:
        return True
    else:
        return False
