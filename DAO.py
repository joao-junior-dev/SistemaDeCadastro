from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Base, Usuario

USUARIO = 'root'
SENHA = 'root'
HOST = 'localhost'
BANCO = 'cadastro'
PORT = '3306'

CONN = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}'

engine = create_engine(CONN)
Session = sessionmaker(bind=engine)
session = Session()

# cria o banco de dados
Base.metadata.create_all(engine)

class DaoUsuario:
    @classmethod
    def ler(cls):
        usuarios = session.query(Usuario).all()
        return usuarios
    @classmethod
    def salvar(cls, nome, email, senha):
        usuario = Usuario(nome=nome,
                          email=email,
                          senha=senha)
        session.add(usuario)
        session.commit()

session.close()