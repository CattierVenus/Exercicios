#Matriz campo
MINA = -1     #'✱'
LIVRE = 0

#Matriz acesso
NAO_ACESSADA = 0 #?
ACESSADA = 1
BANDEIRA = 2

import random

def CriaMatriz(m, n, valor):
    M =[]
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(valor)
        M.append(linha)
    return M

def Embaralha(matriz):
    m = len(matriz)
    n = len(matriz[0])
    for i in range(m):
        for j in range(n):
            x = random.randrange(0,n)
            y = random.randrange(0, m)
            tmp = matriz[i][j]
            matriz[i][j] = matriz[y][x]
            matriz[y][x] = tmp
'''
def CriaCampo(m, n, nminas):
    Campo = CriaMatriz(m, n, LIVRE)
    i,j = 0,0
    for k in range(nminas):
        Campo[i][j] = MINA
        j += 1
        if j == n:
            j = 0
            i += 1
    Embaralha(Campo)
    return Campo
'''
def CriaCampo(m, n, nminas):
    C = [MINA]*nminas + [LIVRE]*(m*n - nminas)
    random.shuffle(C)
    Campo = []
    for i in range(m):
        Campo.append(C[i*n: (i+1)*n])
    return Campo
'''
#Solução complexa demais
def ContaMinas(Campo, lin, col):
    m = len(Campo)
    n = len(Campo[0])
    conta = 0
    if col - 1 >= 0:
        if Campo[lin][col - 1] == MINA:
            conta += 1
    if lin - 1 >= 0 and col - 1 >= 0:
        if Campo[lin-1][col-1] == MINA:
            conta += 1
    if lin+1 < m:
        if Campo[lin+1][col] == Mina:
            conta += 1
    #...
    return conta
'''
def ContaMinas(Campo, lin, col):
    m = len(Campo)
    n = len(Campo[0])
    conta = 0
    for i in range(lin-1, lin+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < m and j >= 0 and j < n:
                if Campo[i][j] == MINA:
                    conta += 1
    return conta

def ContaMinasCampo(Campo):
    m = len(Campo)
    n = len(Campo[0])
    for i in range(m):
        for j in range(n):
            if Campo[i][j] == LIVRE:
                Campo[i][j] = ContaMinas(Campo, i, j)

def TestaBoom(Campo, Acesso):
    m = len(Campo)
    n = len(Campo[0])
    boom = False
    for i in range(m):
        for j in range(n):
            if Campo[i][j] == MINA and Acesso[i][j] == ACESSADA:
                boom = True
    return boom

def TestaVitoria(Campo, Acesso):
    m = len(Campo)
    n = len(Campo[0])
    vitoria = True
    for i in range(m):
        for j in range(n):
            if Campo[i][j] != MINA and Acesso[i][j] != ACESSADA:
                vitoria = False
    return vitoria

def ImprimeTabuleiro(Campo, Acesso):
    m = len(Campo)
    n = len(Campo[0])
    boom = TestaBoom(Campo, Acesso)
    for i in range(m):
        for j in range(n):
            if boom and Campo[i][j] == MINA:
                print('✱  ', end = '')
            elif Acesso[i][j] == BANDEIRA:
                print('P  ', end = '')
            elif Acesso[i][j] == NAO_ACESSADA:
                print('?  ', end = '')
            else: #Se foi acessada
                print('%d  '%(Campo[i][j]), end = '')
        print()

def main():
    print('Lembre-se que: a segunda linha é a número 1, a terceira é 2, etc')
    m = int(input('Digite o n de linhas: '))
    n = int(input('Digite o n de colunas: '))
    nminas = int(input('Digite o n de bombas: '))
    Campo = CriaCampo(m, n, nminas)
    ContaMinasCampo(Campo)
    Acesso = CriaMatriz(m, n, NAO_ACESSADA)
    ImprimeTabuleiro(Campo, Acesso)
    continua = True
    while continua:
        lin = int(input('Digite a linha: '))
        col = int(input('Digite a coluna: '))
        band = input('Bandeira? (s/n) ')
        if band == 's':
            if Acesso[lin][col] == BANDEIRA:
                Acesso[lin][col] = NAO_ACESSADA
            elif Acesso[lin][col] == NAO_ACESSADA:
                Acesso[lin][col] = BANDEIRA
        else: #band == 'n'
            if Acesso[lin][col] != BANDEIRA:
                Acesso[lin][col] = ACESSADA
        
        ImprimeTabuleiro(Campo, Acesso)
        vitoria = TestaVitoria(Campo, Acesso)
        boom = TestaBoom(Campo, Acesso)
        if vitoria or boom:
            continua = False
    
    if vitoria:
        print('Tu é brabo')
    else:
        print('BOOOOOMMMM!')

main()
