
velocidade = int(input('Qual foi a velocidade registrada?'))
taxa_20 = 120 * 0.20
taxa_30 = 150 * 0.30


if velocidade <= 100:
    taxa = 0

elif velocidade <=120:
    taxa = velocidade * 0.20

elif velocidade <=150:
    taxa = (velocidade * 0.30) + taxa_20

else:
    taxa = (velocidade * 0.4) + taxa_20 + taxa_30

print(f'A taxa é de {taxa} reais')

num1 = int(input("Diga um número: "))
num2 = int(input("Diga outro número: "))
num3 = int(input("Diga mais um número: "))
num4 = int(input("Diga mais um número: "))
num5 = int(input("Diga um último número: "))
pares = 0
impares = 0

if num1 % 2 == 0:
    pares = pares + 1

else:
    impares = impares + 1

if num2 % 2 == 0:
    pares = pares + 1

else:
    impares = impares + 1

if num3 % 2 == 0:
    pares = pares + 1

else:
    impares = impares + 1

if num4 % 2 == 0:
    pares = pares + 1

else:
    impares = impares + 1

if num5 % 2 == 0:
    pares = pares + 1

else:
    impares = impares + 1

print(f"A qtd de pares é {pares}")
print(f"A qtd de impares é {impares}")

qtd = 1
senha_correta = '1234'
senha = input("Digite sua senha: ")

while qtd < 3 and senha != senha_correta:
    senha = input("Tente novamente: ")
    qtd += 1

if qtd > 2:
    print("Limite de tentativas atingido")

else:
    print("Seja bem-vindo")

i = 0
soma = 0
while i < 10:
   i = 1 + i
   soma += i
   print(soma)


i = 0
pares = 0
impares = 0
i = int(input("Digite um número:"))
while qtd < 10:
    i = int(input("Digite um número:"))
    qtd += 1
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Esses são os pares: {pares}")
print(f"Esses são os impares: {impares}")



res_corr = "Sim"
res_corr2 = "Sim demais"

resposta = input("A Camila é a mulher mais legal e linda da FIAP?: ")


while not (resposta == res_corr or resposta == res_corr2):
    print("Você é burro e cego")
    resposta = input("A Camila é a mulher mais legal e linda da FIAP?: ")

print("Acertou!!")

i = 100000
ano = 0
while i < 1000000000:
    i = i * 2
    ano += 1

print(ano)

