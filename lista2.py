# Check Point - 1TDSPV - Luiz Kamada

# EX 1
num = int(input("Informe um numero: "))

if num > 10:
    print(num, "É maior que 10")
else:
    print(num, "É menor ou igual a 10")

# EX 2
num_a = int(input("Informe um numero A: "))
num_b = int(input("Informe um numero B: "))

if num_a > num_b:
    print(num_a)
elif num_a < num_b:
    print(num_b)
else:
    print("EMPATE")

# EX 4
gols_a = int(input("Gols A: "))
gols_b = int(input("Gols B: "))        

if gols_a > gols_b:
    print("Time A ganhou")
elif gols_a < gols_b:
    print("Time B ganhou")
else:
    print("Empate")

# EX 5
dias_uteis = 30//7
valor_hora = int(input("Quanto ganha por hora?"))
horas_regular = dias_uteis * 8
horas_extra = int(input("Horas extra total"))
salario_regular = horas_regular * valor_hora
salario_extra = horas_extra * valor_hora * 1,5
salario_total = salario_regular + salario_extra
print("Seu salário é", salario_total)

# EX 6
num_a = int(input("Informe um numero A: "))
num_b = int(input("Informe um numero B: "))

if num_a%num_b == 0:
    print("O numero é divisivel") 
else:
    print("O numero não é divisivel")

# EX 7 
import math
num = float(input("Digite um numero:"))
if math.sqrt(num)*math.sqrt(num) == num:
    print("A raiz quadada de", num, "é", math.sqrt(num))
else:
    print("Não a raiz quadrada")

# EX 8
idade = int(print("Qual é a sua idade ?"))
if idade >= 5 and idade <= 7:
    print("Infantil")
elif idade >= 8 and idade <= 10:
    print("Juvenil")
elif idade >= 11 and idade <= 15:
    print("Adolescente")
elif idade >= 16 and idade <= 30:
    print("Adulto")
else:
    print("Senior") 

# EX 9
num_a = float(input("Digite a: "))
op = input("Informe o operador (+-*/): ")
num_b = float(input("Digite b: "))

if op == "+":
    resultado = num_a + num_b
elif op == "-":
    resultado = num_a - num_b
elif op == "*":
    resultado = num_a * num_b
elif op == "/" and num_a!=0 and num_b!=0:
    resultado = num_a / num_b
else:
    print("Divisão não possivel")

print("O resultado vale",resultado)

# EX 10
import math
a = float(input("Valor A:"))
b = float(input("Valor B:"))
c = float(input("Valor C:"))

delta = b**2 - 4 * a * c
x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print("X1 =", x1, "X2 =", x2)

# EX 11
preco = float(input("Informe o valor:"))
tipo = int(input("Escolha o codigo:"))

if tipo == 1:
    novo_preco = preco * 0.9
elif tipo == 2:
    novo_preco = preco * 0.95
elif tipo == 3:
    novo_preco = preco
elif tipo == 4:
    novo_preco = preco * 1.07

print("O valor pago será", novo_preco)

# EX 12
n_aulas_ministrada = int(input("Numero de aulas ministradas:"))
n_aulas_assistida = int(input("Numero de aulas assistidas:"))
nota_1semestre = float(input("Nota 1 semestre:"))
nota_2semestre = float(input("Nota 2 semestre:"))

if n_aulas_assistida >= (n_aulas_ministrada*0.7):
    resultado = nota_1semestre * 0.4 + nota_2semestre * 0.6
    if resultado >= 5:
        print("Aprovado")
    else:
        print("Reprovado") 
else:
    print("Reprovado")



