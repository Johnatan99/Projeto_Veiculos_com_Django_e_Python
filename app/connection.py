import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    port='3306',
    password='PassWord#123',
    database='dbDengue',
) 
cursor = conexao.cursor()

sql = "select * from municipio"
cursor.execute(sql)
registros = cursor.fatchall() #fatchall realiza a busca dos dados recebidos pela query
print("Tipo retornaado pelo fetchall():"), type(registros)

for registro in registros:
    print("Tipo: ",type(registro)," Conteúdo: ", registro)

cursor.close()
conexao.close()