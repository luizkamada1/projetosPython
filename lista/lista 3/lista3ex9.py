d = float(input("Informe o dinheiro inicial:"))
j = float(input("Informe a taxa de juros mensal:"))
t = int(input("Informe o período de tempo:"))

i = 0 

while i < t:
    d = d * (1 + j)
    i = i + 1

print (d)