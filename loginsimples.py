# login simples 0.1
banco_de_dados = [
    'Admin', 'admin'
]
login = ''
senha = ''


def CampoDeLogin():
    global banco_de_dados
    global login
    global senha
    login_seguranca = False
    while not login_seguranca:
        login = input('Digite seu Usuario: ')
        senha = input('Digite sua senha: ')
        if login in banco_de_dados[0] and senha in banco_de_dados[1]:
            print('Login realizado com sucesso!')
            login_seguranca = True
        else:
            print('Usuario e/ou senha incorretos! tente novamente')
    return


CampoDeLogin()
print(login, senha)

