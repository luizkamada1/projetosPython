n = int(input("Informe um número inteiro positivo:"))

i = 1
somatorio = 1

while i <= n:
    somatorio = somatorio * i
    i = i + 1

print ("O fatorial de", n, "é", somatorio)

