def ordenar_pessoas_basico(lista_pessoas):
    # Implementação do Bubble Sort
    n = len(lista_pessoas)
    for i in range(n):
        for j in range(0, n-i-1):
            # Verifica se o nome da pessoa atual é maior que o próximo nome
            if lista_pessoas[j][0] > lista_pessoas[j+1][0]:
                # Troca as posições
                lista_pessoas[j], lista_pessoas[j+1] = lista_pessoas[j+1], lista_pessoas[j]
            # Se os nomes forem iguais, ordena pela idade
            elif lista_pessoas[j][0] == lista_pessoas[j+1][0] and lista_pessoas[j][1] > lista_pessoas[j+1][1]:
                # Troca as posições
                lista_pessoas[j], lista_pessoas[j+1] = lista_pessoas[j+1], lista_pessoas[j]
    return lista_pessoas

# Exemplo de uso:
lista_pessoas = [('Joao', 25), ('Ana', 25), ('Ana', 30), ('Joao', 20), ('Maria', 22)]
lista_ordenada = ordenar_pessoas_basico(lista_pessoas)
print(lista_ordenada)
