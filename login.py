import psycopg

class Usuario:
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

def existe(usuario):
  # abrir uma conexão com o postgresql
  with psycopg.connect(
    host = "docker-db-1",
    dbname = "pbdi",
    user = "postgres",
    password = "123456"
  ) as conexao:
    # por meio da conexão, obter uma abstração do tipo cursor
    with conexao.cursor() as cursor:
      # por meio do cursor, executar um comando select
      cursor.execute( #in-place
        "select * from tb_usuario where login = %s and senha = %s",
        (usuario.login, usuario.senha)
      )
      # usar um método do cursor para verifiar o resultado produzido pelo select
      result = cursor.fetchone()

  # devolver true ou false, conforme o resultado
  return result != None
