def organiza(conj: list, pos: int):
    #pos = len(conj) - 1
    aux = conj[pos] 

    while conj[pos - 1] > aux and pos > 0:
        conj[pos] = conj[pos - 1]
        pos = pos - 1
    
    conj[pos] = aux

def insertion_sort(lista: list):
    for i in range(1, len(lista)):
        organiza(lista, i)

if __name__ == "__main__":
    list = [4, -2, 0, 7, 10, 5, 6, 3, 7]
    insertion_sort(list)
    print(list)

# O(n) -> Busca simples
# O(log n) -> Busca binaria
