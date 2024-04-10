n = int(input("Informe o número:"))

i = 0
num = 1

if n == 1 or n ==2:
        print ("O n-ésimo número da sequência de Fibonacci é 1")
elif n > 2:
    while i <= n:
        num  = (num - 1) + (num -2)
        i = i + 1
        print(acumulado)
