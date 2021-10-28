# calculadora em desenvolvimento
# função soma funcionando
# versão 0.1
from time import sleep
operador = 'n'

def menu():
    global operador
    print('~'*26)
    print('| Calculadora Simples  V1|\n'
          '|------------------------|\n'
          '| [ + ] - Soma           |\n'
          '| [ - ] - Subtração      |\n'
          '| [ * ] - Multiplicação  |\n'
          '| [ / ] - Divisão        |\n'
          '| [ s ] - Sair           |')
    print('~'*26)
    operador = input('Escolha o operando: ')
    return operador


def soma():
    global asoma
    asoma = 0
    n1 = False
    while not n1:
        n1 = input('Digite o primeiro número: ')
        if n1.isnumeric():
            asoma += int(n1)
        else:
            print('Digite apenas números!')
            n1 = False
            limpa()
    n2 = False
    while not n2:
        n2 = input('Digite outro número para somar: ')
        if n2.isnumeric():
            n2 = int(n2)
            asoma += n2
            outro = input('Digite "s" para sair ou "+" para adicionar mais números. ')
            if outro == '+':
                n2 = False
                limpa()
                print('primeiro número: ', asoma)
        else:
            limpa()
            print('Digite apenas números inteiros!')
            sleep(2)
            n2 = False
            limpa()
            print('primeiro número: ', asoma)

    print('A soma entre os números é: ', asoma)



def limpa():
    print('\n'*100)


while operador not in 'Ss':
    menu()
    if operador == '+':
        soma()
    elif operador == '-':
        pass
    elif operador == '*':
        pass
    elif operador == '/':
        pass
    elif operador in 'Ss':
        pass
    else:
        print('Erro!'
              'Tu digitou um operador invalido, tente novamente ou digite "s" para sair..')
        sleep(1)
        print('.', end= ' ')
        sleep(1)
        print('.', end = ' ')
        sleep(1)
        print('.')
        limpa()
