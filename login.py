import psycopg

class Usuario:
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

def existe(usuario):
  # abrir uma conexão com o postgresql
  with psycopg.connect(
    host = "localhost",
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

def insere(usuario):
  # abrir uma conexão com o postgresql
  with psycopg.connect(
    host = "docker-db-1",
    dbname = "pbdi",
    user = "postgres",
    password = "123456"
  ) as conexao:
    # por meio da conexão, obter uma abstração do tipo cursor
    with conexao.cursor() as cursor:
      # por meio do cursor, executar um comando insert
      cursor.execute( #in-place
        "insert into tb_usuario (login, senha) values (%s, %s);",
        (usuario.login, usuario.senha)
      )
      # usar um método do cursor para verifiar o resultado produzido pelo insert
      result = cursor

  # devolver true ou false, conforme o resultado
  return result != None

def menu():
  texto = "0-Fechar\n1-Login\n2-Logoff\n3-Inserir Usuário\n"
  usuario = None
  op = int(input(texto))
  while op!= 0:
    if op == 1:
      login = input("Digite seu login\n")
      senha = input("Digite sua senha\n")
      usuario = Usuario(login, senha)
      print("Usuário OK!" if existe(usuario) else "Usuário NOK!")
    elif op == 2:
      usuario = None
      print("Logoff realizado com sucesso")
    elif op == 3:
      login = input("Digite o login\n")
      senha = input("Digite a senha\n")
      usuario = Usuario(login, senha)
      result = insere(usuario)
      if result:
        print("Usuário cadastrado com sucesso")
      else:
        print("Ocorreu um erro")
    op = int(input(texto))
  else:
    print("Até mais")

def main():
  # login = "admin"
  # senha = "admin"
  # usuario = Usuario(login, senha)
  # print("Existe" if existe(usuario) else "Não existe")
  menu()

main()
