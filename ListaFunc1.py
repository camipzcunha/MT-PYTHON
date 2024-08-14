'''nome= input("Diga seu nome: ")
primeiro_numero = int(input(f"{nome}, diga o primeiro número: "))
segundo_numero = int(input(f"{nome}, diga um segundo número: "))
soma = primeiro_numero + segundo_numero
print(f"A soma entre {primeiro_numero} e {segundo_numero} é {soma}")
mult = primeiro_numero * segundo_numero
print(f"A multiplicação entre o primeiro e o segundo número é igual a {mult}")
sub = primeiro_numero - segundo_numero
print(f"A subtração entre o primeiro e o segundo número é igual a {sub}")
div = primeiro_numero/segundo_numero
print(f"A divisão entre o primeiro e o segundo número é igual a {div}")
frase = "O"
print(frase)
frase = frase + " Palmeiras"
print(frase)
frase = frase + " foi"
print(frase)
frase = frase + " campeão"
print(frase)

///////////////////////////////////////////////////
primeiro_numero = 2
segundo_numero= 3
a = primeiro_numero == segundo_numero
print(f"A comparação {primeiro_numero} == {segundo_numero} é {a}")
a = primeiro_numero > segundo_numero
print(f"A comparação {primeiro_numero}>{segundo_numero} é {a}")
a = primeiro_numero < segundo_numero
print(f"A comparação {primeiro_numero} < {segundo_numero} é {a}")
a = primeiro_numero != segundo_numero
print(f"A comparação {primeiro_numero} é diferente de {segundo_numero} é {a}")

//////////////////////////////////////////////////////////////
a = 2
b = 3
c = 4
d = 5
print(f"{a}>{b} or {c} > {d}, ou seja, {a>b} or {c>d} é {a>b or c>d}")
print(f"{a}<{b} or {c} > {d}, ou seja, {a < b} or {c>d} é {a<b or c>d}")
print(f"{d}>{a} or {b} < {c}, ou seja, {d > a} or {b<c} é {d>a or b<c}")
print(f"{a}>{b} and {a}<{d} é {a>b and a<d}")

senha = input("Insira sua senha: ")
senha_correta = '1234'
if senha == senha_correta:
    print("Acertou")


 Tudo que deve acontecer no IF deve estar identado

idade = int(input("Diga sua idade: "))
if idade < 18:
    print("Não beba")
else:
    print("Pode encher a cara")


letra = input("Insira uma letra: ")
if {letra} == {'a' and 'e' and 'i' and 'o' and 'u'}:
    print("É vogal")
else:
    print("É consoante")

    ///////////////////////////////////////////////
'''

'''salario = float(input("Qual o seu salario atual em R$? "))

if salario < 1093.98:
    print(f"Sua aliquota é isenta. Seu salário é de {salario}")

elif salario<= 2826.65:
    desc = 0.075

elif salario<=3751.05:
    desc = 0.15

elif salario <=4664.68:
    desc = 0.225

else:
    desc = 0.275

desconto = salario * desc
sal = salario - desconto
print(f"Seu salário é de {sal}")

'''
