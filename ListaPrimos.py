def primos(n):
    for i in range(2,n):
        if n % i == 0:
            return False 
        return True

def lista_primos(n):
    resultado = []
    for i in range(2,n):
        if primos(i):
            resultado.append(i)
    return resultado

print(lista_primos(100))
