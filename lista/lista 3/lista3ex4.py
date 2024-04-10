# Exercicio 4

n = int(input("Quantos numeros tem:"))
num_neg = 0
num_pos = 0
i = 0 

while i < n:
    valor = float(input("Informe o número:"))
    if valor >= 0:
        num_pos = num_pos + 1
    elif valor < 0:
        num_neg = num_neg + 1
    i = i + 1

print ("Possuem", num_pos, "valores positivos e", num_neg, "valores negativos")