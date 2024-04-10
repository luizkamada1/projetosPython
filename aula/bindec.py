bin = int(input("Informe um número da base binária:"))

i = 0
n = len(str(bin))
acumulado = 0

while i < n:
    dig = bin % 10
    if dig == 1:
        acumulado = acumulado + 1 * 2**i
    bin = bin // 10
    i = i + 1

print (acumulado)