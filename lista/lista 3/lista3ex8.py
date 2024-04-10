# Exercicio 8


n = int(input("Informe um número:"))
i = 1
divisao = 0 
while i <= n:
    if n % i == 0:
        print(i)
        divisao = divisao + 1

    i = i + 1

if divisao == 2:
    print("O número é primo")
else:
    print("O número não é primo")

