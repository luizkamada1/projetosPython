n = int(input("Digite o número de elementos na sequência: "))

numeros = []

print("Digite os números da sequência:")
for i in range(n):
    numero = float(input(f"Número {i + 1}: "))
    numeros.append(numero)

soma_maiores_que_50 = 0
contagem_menores_que_100 = 0

for numero in numeros:
    if numero > 50:
        soma_maiores_que_50 += numero
    if numero < 100:
        contagem_menores_que_100 += 1

print(f"A somatória de números maiores que 50 é: {soma_maiores_que_50}")
print(f"O número de elementos menores que 100 é: {contagem_menores_que_100}")
