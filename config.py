import cx_Oracle

username = 'metalbi'
password = 'metalbi'
host = '10.0.2.111'         # exemplo: 'localhost' ou '192.168.0.10'
port = 1521               # porta padrão Oracle
service_name = 'METALSINOS'

dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)

try:
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)
    print("Conexão estabelecida com sucesso!")

    # Criar cursor e executar uma query
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM programacao_diaria pd inner join metalsinos.pcm_temp_coletor ptc on ptc.talao = pd.talao")
    for row in cursor:
        print(row)

    # Fechar conexões
    cursor.close()
    connection.close()

except cx_Oracle.DatabaseError as e:
    print("Erro ao conectar ao banco de dados:", e)