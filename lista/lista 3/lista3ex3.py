# Exercicio 3

n = int(input("Informe quantidade de alunos:"))
i = 0
somatorio1 = 0
somatorio2 = 0
n1 = 0
n2 = 0
while i < n:
    nota = float(input("Informe a nota:"))
    if nota >= 0 and nota < 5:
        somatorio1 = somatorio1 + nota
        n1 = n1 + 1
    elif nota >= 5 and nota < 10:
        somatorio2 = somatorio2 + nota
        n2 = n2 + 1
    i = i + 1

media1 = somatorio1 / n1
media2 = somatorio2 / n2
print("A média é das notas entre 0 e 5 é ", media1)
print("A média é das notas entre 5 e 10 é ", media2)