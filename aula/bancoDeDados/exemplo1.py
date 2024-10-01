# pip3 install oracledb

# Connection 
# Statement/ PreperedStatment (para o CRUD)

import oracledb

conexao = oracledb.connect(user='pf0313',
                           password='professor#23',
                           dsn='oracle.fiap.com.br/orcl')

print(conexao.version)
cursor = conexao.cursor()

cursor.execute('select sysdate from dual')
registro = cursor.fetchone() 
# fetch para trazer o resultado
# fetchone() para trazer um unico registro
# print(registro[0])

# cursor.execute('select * from medico')
cursor.execute('select id, nome, crm, especialidade from medico order by id')
registro = cursor.fetchall()
# fetchall() pega todos os registros
# fetchmany(size) recupara uma quantidade size ou padrão. memoria não estora, vai aos poucos
# [] -> lista
# () -> tuplas
# print(registro)
for med in registro:
    print(med)

cursor.close()
conexao.close()



