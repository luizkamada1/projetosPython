n = int(input("Digite o número de elementos na sequência: "))

# Entrada dos elementos da sequência
sequencia = []
print(f"Digite os {n} elementos da sequência:")
for i in range(n):
    elemento = int(input(f"Elemento {i+1}: "))
    sequencia.append(elemento)

# Inicialização do contador de segmentos
if n > 0:
    segmentos = 1  # A primeira entrada já conta como um segmento
else:
    segmentos = 0

# Contagem dos segmentos de números iguais consecutivos
for i in range(1, n):
    if sequencia[i] != sequencia[i - 1]:
        segmentos += 1

print(f"O número de segmentos de números iguais consecutivos é: {segmentos}")
