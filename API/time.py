
def encontra_time(nome: str) -> dict:
    pass

#{'nome': 'Palmeiras', 'vitorias': 2, 'empates': 1, 'derrotas': 0, 'gols_contra': 5, 'gols_pro': 9, 'id': 23}

#{'visi': 'Palmeiras', 'casa': 'Santos', 'gv':1, 'gc':3, 'rodada': 1}

def cadastra_partida(jogo: dict):
    time_casa = encontra_time(jogo['casa'])
    time_visi = encontra_time(jogo['visi'])
