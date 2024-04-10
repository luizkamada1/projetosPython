#Exercicio 2

n = int(input("Informe quantidade de alunos:"))
i = 0
somatorio = 0
while i < n:
    nota = float(input("Informe a nota:"))
    somatorio = somatorio + nota
    i = i + 1

media = somatorio / n
print("A média é ", media)