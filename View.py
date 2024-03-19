from Controller import ControllerCadastro

if __name__ == '__main__':
    while True:
        decisao = int(input('Bem-vindo\n'
                            'Digite (1) para cadastrar\n'
                            'Digite (2) para logar\n'
                            'Digite (3) para sair\n'))
        if decisao == 1:
            nome = input('Digite seu nome: ')
            email = input('Digite seu email: ')
            senha = input('Digite a sua senha: ')
            usuarios = ControllerCadastro()
            usuarios.cadastrar(nome, email, senha)
        elif decisao == 2:
            email = input('Digite o seu email: ')
            senha = input('Digite a sua senha: ')
            usuarios = ControllerCadastro()
            usuarios.login(email, senha)
        else:
            break

