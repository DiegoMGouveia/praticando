# login simples 0.1
from time import sleep
banco_de_dados = [
    'Admin', 'admin'
]
login = ''
senha = ''


def limpa():
    print('\n'*100)


def CampoDeLogin():
    global banco_de_dados
    global login
    global senha
    login_seguranca = False
    limpa()
    while not login_seguranca:
        login = input('Digite seu Usuario: ')
        senha = input('Digite sua senha: ')
        limpa()
        if login in banco_de_dados[0] and senha in banco_de_dados[1]:
            print('Login realizado com sucesso!')
            login_seguranca = True
        else:
            print('Usuario e/ou senha incorretos! tente novamente')
        sleep(2)
        limpa()
    return


CampoDeLogin()
print(login, senha)

