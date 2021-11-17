#exercicio 93 curso de python

lista_de_tarefa = ['Estudar', 'Brincar', 'trabalhar']
desfeito = []


menu_0 = '''
    |_______________________|
    | [1] - Adicionar tarefa|
    | [2] - Listar tarefas  |
    | [3] - Desfazer tarefa |
    | [4] - Refazer tarefa  |
    | [5] - Sair
    |_______________________|
    
    Digite uma opção: '''


def adicionar(kwargs):
    a = input('Qual tarefa: ')
    kwargs.append(a)
    return


def listar(lista):
    for x in lista:
        print(x)


def desfazer(kwargs, kwargs2):
    try:
        for x in kwargs:
            t = x
        kwargs2.append(t)
        kwargs.pop()
        return kwargs and kwargs2
    except UnboundLocalError:
        print('não tem valores a desfazer')


def refazer(kwargs, kwargs2):
    try:
        for x in kwargs2:
            t = x
        kwargs.append(t)
        kwargs2.pop()
        return kwargs and kwargs2
    except UnboundLocalError:
        print('não tem valores a refazer')


while True:
    opc_menu = input(menu_0)
    if opc_menu == '1':
        adicionar(lista_de_tarefa)
    elif opc_menu == '2':
        listar(lista_de_tarefa)
    elif opc_menu == '3':
        desfazer(lista_de_tarefa, desfeito)
        listar(lista_de_tarefa)
    elif opc_menu == '4':
        refazer(lista_de_tarefa, desfeito)
        listar(lista_de_tarefa)
    elif opc_menu == '5':
        break
    else:
        print('Digite apenas as opções do menu!')


