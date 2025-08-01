import cx_Oracle

username = 'metalbi'
password = 'metalbi'
host = '10.0.2.111'         # exemplo: 'localhost' ou '192.168.0.10'
port = 1521               # porta padrão Oracle
service_name = 'METALSINOS'

dsn_tns = cx_Oracle.makedsn(host, port, service_name=service_name)


conn = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)
cursor = conn.cursor()
cursor.execute("SELECT * FROM METALSINOS.GEN_FOTOS x WHERE x.CODIGO = 5315")
colunas = [desc[0] for desc in cursor.description]
linhas = cursor.fetchall()   

def formatar_celula(valor):
    if hasattr(valor, "strftime"):  # datetime
        return valor.strftime("%Y-%m-%d %H:%M:%S")
    return valor


# Criar HTML
html = "<table border='1'>\n"
html += "  <thead><tr>" + "".join(f"<th>{col}</th>" for col in colunas) + "</tr></thead>\n"
html += "  <tbody>\n"
for linha in linhas:
    html += "    <tr>" + "".join(f"<td>{formatar_celula(celula)}</td>" for celula in linha) + "</tr>\n"
html += "  </tbody>\n</table>"

# Exibir ou salvar
print(html)

# (Opcional) salvar como arquivo
with open("teste.html", "w", encoding="utf-8") as f:
    f.write(html)