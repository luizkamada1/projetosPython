import banco

clas = input("Genero: ")
filmes = banco.consulta_filme(clas)

for f in filmes:
    print(f)