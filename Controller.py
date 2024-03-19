import re, bcrypt
from DAO import DaoUsuario

def validar_email(email):
    # limpa espaços antes e depois do email
    email = email.strip()
    # Expressão regular para validar o formato do e-mail
    padrao = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'

    # Verificar se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False


def validar_senha(senha):
    # limpa espaços antes e depois da senha
    senha = senha.strip()
    # Padrão para validar a senha
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\W]{8,}$'

    # Verificar se a senha corresponde ao padrão
    if re.match(padrao, senha):
        return True
    else:
        return False


def criptografar_senha(senha):
    # Gere um salt aleatório
    salt = bcrypt.gensalt()

    # Criptografa a senha usando o salt
    senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), salt)

    return senha_criptografada

class ControllerCadastro:

    def cadastrar(self, nome, email, senha):
        # Limpeza dos parâmetros
        nome = nome.strip()
        # 1º - Verifica se e o e-mail já existe
        usuarios = DaoUsuario.ler()
        for usuario in usuarios:
            if usuario.email == email:
                raise ValueError('Email já cadastrado')
        # 2º verificação dos dados
        if len(nome) < 2 or len(nome) > 100:
            raise ValueError('Nome inválido')
        if not validar_email(email):
            raise ValueError('Email inválido')
        if not validar_senha(senha):
            raise ValueError('''
            A senha deve ter atender os seguintes criterios:
            Deve ter no mínimo 8 caracteres.
            Deve conter pelo menos uma letra maiúscula.
            Deve conter pelo menos uma letra minúscula.
            Deve conter pelo menos um dígito.
            Pode conter caracteres especiais.
            ''')

        # se o usuário passar por todos os testes, então salvaremos no bd
        DaoUsuario.salvar(nome, email, criptografar_senha(senha))
        print('usuario cadastrado com sucesso')

    def login(self, email, senha):
        if not validar_email(email):
            raise ValueError('Email digitado incorretamente')

        usuarios = DaoUsuario.ler()
        for usuario in usuarios:
            if usuario.email == email:
                if bcrypt.checkpw(senha.encode('utf-8'), usuario.senha.encode('utf-8')):
                    print('Usuario logado com sucesso')

