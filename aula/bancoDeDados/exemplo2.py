import oracledb

con = oracledb.connect(user='pf0313',
                           password='professor#23',
                           dsn='oracle.fiap.com.br/orcl')
cur = con.cursor()

sql = '''insert into empregado(numero, nome, cargo, departamento, salario,
            data_contratacao) values(:numero, :nome, :cargo, :departamento,
            :salario, to_date(:data_contratacao, 'MM-DD-YYYY'))'''

# parametrizar no Java (?, ?)
# parametrizar no Pyhton (:parametro1, :parametro2)

info = {'numero': 2756, 'nome': 'Manuel Ferreira', 'salario':5400.20, 'cargo': 'Diretor', 'departamento': 'Reitor',
        'data_contratacao': '10-23-2008'}

cur.execute(sql, info)
con.commit()
cur.close()
con.close()