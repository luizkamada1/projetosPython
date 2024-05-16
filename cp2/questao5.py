entrada = input("Digite uma string: ")

invertida = ''

for i in range(len(entrada) - 1, -1, -1):
    invertida += entrada[i]

print("String invertida:", invertida)
