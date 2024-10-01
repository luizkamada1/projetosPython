def bubble_sort(lista):
    n = len(lista)
    # Percorrer todos os elementos da lista
    for i in range(n):
        # Últimos i elementos já estão no lugar
        for j in range(0, n-i-1):
            # Trocar se o elemento encontrado for maior que o próximo elemento
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Exemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
sorted_lista = bubble_sort(lista)
print("Lista ordenada:", sorted_lista)
