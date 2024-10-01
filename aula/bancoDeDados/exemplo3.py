import oracledb

con = oracledb.connect(user='pf0313',
                           password='professor#23',
                           dsn='oracle.fiap.com.br/orcl')
cur = con.cursor()

sql = '''update empregado set nome = :name, cargo = :job_title, 
        departamento = :department, salario = :salary,
        data_contratacao = to_date(:hiring_date, 'YYYY-MM-DD') where numero = :id'''

info = {'id': 1000, 'name': 'João Amorim', 'salary':50.30, 'job_title': 'Nada', 'department': 'Nenhum',
        'hiring_date': '03-07-2002'}

cur.execute(sql, info)
con.commit()
cur.close()
con.close()