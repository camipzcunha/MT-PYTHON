def cria_naipe(naipe):
    cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    resposta = []
    for carta in cartas:
        carta_naipe = carta + naipe
        resposta.append(carta_naipe)
    return resposta

'''def cria_baralho():
    resposta = []
    naipes =['c', 'o', 'e', 'p']
    cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for naipe in naipes:
        for carta in cartas:
            resposta.append(carta + naipe)
    return resposta'''

def cria_baralho():
    resposta = []
    for naipe in ['c', 'o', 'e', 'p']:
        baralho = cria_naipe(naipe)
        for carta in baralho:
            resposta.append(carta)
    return resposta

b = cria_baralho()
