if __name__ == '__main__':
    quadro = {
        "China": [45,32,16],
        "Grã Betanha": [29,16,12],
        "Estados Unidos": [15,19,11],
        "Brasil": [13,9,20],
        "França": [11,10,13]
    }

    # Outra forma
    medalhas = {}
    medalhas["China"] = [45,32.16]

    pais = input("Informe um país: ")
    ouro = int(input("Ouro: "))
    prata = int(input("prata: "))
    bronze = int(input("bronze: "))

    if not pais in medalhas:
        medalhas[pais] = [ouro, prata, bronze]
    else: 
        print("Não foi possivel inserir o pais")

    for chave in medalhas.keys():
        print(chave, "=>", medalhas[chave])

del medalhas['canada']
print(medalhas)