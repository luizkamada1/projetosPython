# Exercicio 6

estudante = 1
nota21 = 0
nota50 = 0
menor_nota = 0
maior_nota = 0 

while estudante <= 20:
    questao = 1
    nota = 0
    while questao <= 70:
        print ("Questão", questao)
        acerto = int(input("Errou,digite 0. Acertou,digite 1:"))
        if acerto == 1:
            nota = nota + 1
        questao = questao + 1
        
    print ("Nota do Estudante", estudante, "é", nota)

    if menor_nota > nota:
        menor_nota = nota
    elif maior_nota < nota:
        maior_nota = nota

    if nota >= 21 and nota <= 50:
        nota21 = nota21 + 1 
    elif nota > 50:
        nota50 = nota50 + 1
    estudante = estudante + 1

print ("Menor nota é:", menor_nota)
print ("Maior nota é:", maior_nota)
print (nota21/20, "Acertaram entre 21 e 50")
print (nota50/20, "Acertaram mais que 50")

