'''Comecemos fazendo um desenho de uma unica linha, com vários pontos. Para isso,
usaremos a funcao linha(n)


Por exemplo, linha(3) deve retornar [['.','.','.']]

Isso representa o seguinte desenho:
...'''

''
def linha(largura):
    pass 
    linha = []
    for i in range(largura):
       linha.append('.')
    return linha

'''print(linha(3)) # deve retornar [['.','.','.']]'''


def duas_linhas(largura):
    pass 
    lista = []
    for i in range(2):
        lista.append(linha(largura))    
    return lista




def varias_linhas(largura, altura):
    pass 
    lista = []
    for i in range(altura):
        lista.append(linha(largura))
        lista.append('\n')
    return lista


def mostra_lista(lista):
    pass 
    string = ''
    for i in lista: 
        string+=i
    return string

def mostra_listas(lista_de_listas):
    pass
    lista = []
    for i in lista_de_listas:
        lista.append(mostra_lista(i))
    return lista


mapa = [['.','b','.'],
        ['a','.','.'],
        ['.','.','c'],
        ['.','.','.']]

def primeira_linha(mapa):
    pass
    return mapa[0]

def linha_n(mapa, linha):
    pass
    return mapa[linha]

def posicao(mapa,x,y):
    pass
    return mapa[x][y]

def coloca(mapa,n_linha,n_coluna,simbolo):
    pass
    mapa[n_linha][n_coluna] = simbolo
    return mapa

def coloca(mapa,n_linha,n_coluna,simbolo):
    pass
    mapa[n_linha][n_coluna] = simbolo
    return mapa

def marca_linha(mapa,n_linha,simbolo):
    pass
    for i in range(len(mapa[n_linha])):
        mapa[n_linha][i] = simbolo
    return mapa

def marca_coluna(mapa,n_coluna,simbolo):
    pass
    for i in range(len(mapa)):
        mapa[i][n_coluna] = simbolo
    return mapa

'''Façamos agora uma função que monta um tabuleiro de xadrez.
Ou seja tabuleiro_xadrez(4) produz:

x.x.
.x.x
x.x.
.x.x
'''

def tabuleiro_xadrez(tamanho):
    pass
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if (i+j)%2 == 0:
                linha.append('x')
            else:
                linha.append('.')
        tabuleiro.append(linha)
    return tabuleiro

print(tabuleiro_xadrez(7))
