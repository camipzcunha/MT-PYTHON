'''i = 0
soma = 0
while i < 100:
    i += 1
    soma += i
print(soma)


#Programa nota
nota = int(input("Diga sua nota: "))
while nota>10:
    print("Nota inválida.")
    nota = int(input("Diga sua nota: "))

print(f"Sua nota é {nota}")


#Programa validador
estado_civil = input(("Qual seu estado civil? Digite s, c, d ou v. "))
while not (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'd' or estado_civil == 'v'):
    print("Por favor, digite uma das opções.")
    estado_civil = input("Qual seu estado civil? Digite s, c, d ou v. ")
sexo = input('Qual seu sexo? Digite f para feminino e m para masculino: ')
while not (sexo == 'm' or sexo == 'f'):
    print("Por favor, digite uma das opções.")
    sexo = input('Qual seu sexo? Digite f para feminino e m para masculino: ')
nome = input('Qual seu nome? ')
while (len(nome))<3:
    print('Informe mais que 3 caracteres.')
    nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade?'))
while idade > 150:
    print('Idade inválida.')
    idade = int(input('Qual sua idade?'))
salario = float(input('Qual o seu salário?'))
while salario <= 0:
    print('Salário inválido.')
    salario = float(input('Qual o seu salário?'))

print(f'Suas informações são: {nome}, {idade}, {salario}, {sexo}, {estado_civil}')



popA=80000
popB=200000

ano = 0

while popA < popB:
    taxaA = 0.03*popA
    taxaB = 0.015*popB
    popA = popA + taxaA
    popB = popB + taxaB
    ano = ano + 1

print(ano)


#Soma e média
tentativa = 0
soma = 0
while tentativa < 5:
    numero = int(input('Diga um número: '))
    soma += numero
    tentativa = tentativa + 1

print(soma)
print(soma/tentativa)


#Inteiros
num1 = int(input("Diga um número: "))
num2 = int(input("Diga outro número: "))
intervalo = num1

while intervalo < num2:
    print(intervalo)
    intervalo+=1


#Username and password

username = input('Nome de usuário: ')
password = input('Crie uma senha: ')

while password == username:
    print('A senha não pode ser igual ao nome de usuário.')
    username = input('Nome de usuário: ')
    password = input('Crie uma senha: ')
print(f'Bem vindo {username}')


#Tabuada
num = int(input('Diga um número: '))
i = 1
while i < 11:
    print(num*i)
    i+=1


#Fibonacci
a = 1
b = 1
c = 0
i = 0
position = int(input('Qual a posição desejada?: '))
while i < position:
    c = a + b
    a = b
    b = c
    i += 1
    print(c)


#Pares e ímpares
i = 0
par=0
impar=0
while i<3:
    num=int(input('Diga um número: '))
    if num %2 == 0:
        par+=1
    else:
       impar+=1
    i+=1
print(f'Pares são {par}')
print(f'Impares são {impar}')


#Factorial

num=int(input('Diga um número: '))
i = num-1
while i > 0:
    num = num * i
    i -= 1
print(num)
'''

#Primos
num=int(input('Diga um número: '))
while True:
    num/num and num/1
    print('É primo')
    break
print('Não é primo')
