#Exercício 1
num1= int(input("Escreva um numero: "))
num2= int(input("Escreva outro numero: "))
if num1>num2:
    print(f"O maior número é {num1}")
else:
    print(f"O maior número é {num2}")


#Exercício 2
ano = int(input("Insira seu ano de nascimento: "))
anoat = 2024
idade = anoat - ano
if idade>=18:
    print("Você vota esse ano...")
else:
    print("Você não vota seu besta")
#Exercício 3

senha = input("Insira a senha: ")
senha_correta = '1234'
if senha == senha_correta:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

#Exercício 4
qtd = int(input("Quantas maçãs você comprou branca de neve?: "))
if qtd < 12:
    m = 0.30
else:
    m = 0.25
valor_final = qtd * m 
print(f"O valor total é de R$: {valor_final}")


#Exercício 5
a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))

if a>b and a>c:
    aux = a
    a = c
    c = aux

elif b>c:
    aux = c
    c = b
    b = aux

if a>b:
    aux = a
    a = b
    b = aux

print(a, b, c)


#Exercício 6
sexo = int(input("Qual seu sexo? Considere '1' para feminino e '2' para masculino: "))
altura = float(input("Qual sua altura em M?: "))

if sexo == 2:
    peso = (72.7* altura)-58
    
else:
    peso = (62.1* altura)-44.7

print(f"Este é seu peso ideal em kg: {peso}")

#Exercício 7
qtd_lados = int(input("Qual o número de lados do seu polígono?: "))
med_lado = float(input("Qual a medida do lado em cm?: "))
perimetro = qtd_lados * med_lado

if qtd_lados == 3:
        print(f"Esse é o perimetro: {perimetro}. É um triângulo")

elif qtd_lados == 4: 
     print(f"Esse é o perimetro: {perimetro}. É um quadrado")

elif qtd_lados == 5: 
    print(f"Esse é o perimetro: {perimetro}. É um pentágono")

elif qtd_lados < 3:
      print("Não é um polígono")

else:
      print("Polígono não identificado")

#Exercício 9
a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))

if a>b and a>c:
    print(f"{a} é o maior de todos")
elif b>c:
    print(f"{b} é o maior de todos")
else:
    print(f"{c} é o maior de todos")


#Exercício 10
lado1= int(input("Diga o valor do primeiro lado: "))
lado2= int(input("Diga o valor do segundo lado: "))
lado3= int(input("Diga o valor do terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print("É equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("É isósceles")
else:
    print("É escaleno")

#Exercício 11
ang1 = int(input("Qual o primeiro ângulo?: "))
ang2 = int(input("Qual o segundo ângulo?: "))
ang3 = int(input("Qual o terceiro ângulo?: "))

if ang3 == 90 or ang2 == 90 or ang3 == 90:
    print("Triângulo retângulo")
elif ang3 > 90 or ang2 > 90 or ang3 > 90:
     print("Triângulo obtuso")
else:
    print("Agudo")

#Exercício 12
vel = int(input("Qual foi a velocidade registrada?: "))
multa_
if vel >= 100 and vel <= 120:
    multa = vel * 0,2

elif vel<=150:
    multa = multa + (vel*0,3)
