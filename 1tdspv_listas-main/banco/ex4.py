import banco

filme = {}
filme['titulo'] = 'O Jogo da Imitação'
filme['diretor'] = 'Morten Tyldum'
filme['nota'] = 9.4
filme['sinopse'] = 'Governo do Reino Unido arregimenta, durante a Segunda Guerra Mundial, uma turma de cientistas para decifrar o código Enigma, usado pelos oficiais alemães para enviar mensagens aos submarinos. Entre os cientistas está o matemático Alan Turing, que não consegue se relacionar com os colegas, porém em pouco tempo está liderando a turma na construção de uma uma máquina que analise todas as variações do Enigma a tempo de os britânicos se anteciparem'
filme['genero'] = 'suspence'
filme['classificacao'] = '14 anos'
filme['id'] = 1
filme['data_lancamento'] = '14-11-2014'

banco.altera_filme(filme)