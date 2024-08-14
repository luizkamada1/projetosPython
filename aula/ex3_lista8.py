import busca_simples

#para cada valor da lista A:
# faço uma busca do valor em resp
# se valor não esta em resp
# adiciono valor em resp
#retorno resp

def elimina_repeditos(a):
    resp = []
    for valor in a:
        ret = busca_simples.busca(resp,valor)
        if ret == -1:
            resp.append(valor)
        return resp

lst = [2, 4, 9, 3, 4, 2, 1, 0, 6, 8]
ret = elimina_repeditos(lst)
print("Resposta", ret)
