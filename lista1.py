# LISTA 1
# TESTEEEEEEE
# EX 2
nome = input("Qual é o seu nome?")
sobrenome = input("Qual é o seu sobrenome?")
print(nome, sobrenome)

# EX 3
nome = input("Qual é o seu nome?")
valor = input("Qual ano você nasceu?")
ano_nascimento = int(valor)
idade = 2024 - ano_nascimento
print(nome, "tem (ou terá) ", idade)

# EX 4
valor = input("Primeiro Número?")
num1 = int(valor)
valor = input("Segundo Número?")
num2 = int(valor)

soma = num1 + num2
multiplicacao = num1 * num2
divisao_inteira = num1 // num2
resto_divisao = num1 % num2

print("Soma =", soma, "; Multiplicação =", multiplicacao, "; Divisão Inteira = ", divisao_inteira, "; Reston da Divisão = ", resto_divisao)

#EX 5
valor = input("X = ")
x = int(valor)
valor = input("Y = ")
y = int(valor)

print("X elevado a Y =", x**y)

#EX 6
pi = 3.141592
valor = input("raio")
raio = float(valor)
area = pi * raio**2
print ("A área do circulo é ", area)

#EX 7 
valor = input("Numero = ")
numero = int(valor)
dezena = numero//10
unidade = numero%10
print("Dezena = ", dezena, "Unidade = ", unidade)

#EX 8
valor = input("Camisas = ")
camisas = int(valor)
valor = input("Calças = ")
calcas = int(valor)
valor = input("Sapatos = ")
sapatos = int(valor)
combinacao = camisas * calcas * sapatos
print("A combinações possiveis são = ", combinacao)

#EX 9 
valor = input("Preço = ")
preco = float(valor)
valor = input("Desconto decimal = ")
desconto_percentual = float(valor)
desconto = preco * desconto_percentual
novo_preco = preco - desconto
print ("Novo preço como desconto é ", novo_preco)

#EX 10
valor = input("Distância em metro = ")
distancia = float(valor)
valor  = input("Tempo percorrido = ")
tempo = float(valor)
velocidade_m = distancia/tempo
velocidade_km = velocidade_m * 3.6
print(f"Velocidade m/s é {velocidade_m:.3f}")
print(f" Velocidade km/h é {velocidade_km:.3f}")

#EX 11
valor = input("Salário inicial = ")
salario_inicial = float(valor)
valor = input("Salário final = ")
salario_final = float(valor)
aumento = salario_final/salario_inicial
print("O aumento foi de = ", aumento)

#EX 12
soma = 0
rm = int(input("Qual é o seu RM?"))

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

dig = rm % 10
soma = soma + dig
rm = rm // 10

print("A soma do RM é", soma)

#EX 13
nota_nac = float(input("Nota NAC:"))
nota_am = float(input("Nota AM:"))
nota_ps = float(input("Nota PS:"))
media = (2 * nota_nac + 3 * nota_am + 5 * nota_ps)/10
print("A média da disciplina = ", media)

#EX 4 
avista = float(input("Valor à vista:"))
parcela = float(input("Valor de cada parcela:"))
parcela = 10* parcela
desconto = 1 - (avista/parcela)
print("O valor do desconto foi de:", desconto)



