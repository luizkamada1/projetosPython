def verifica_ordem(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

if __name__ == '__main__':
    lista = [1, 2, 3, 7, 5]
    print(verifica_ordem(lista))
    
