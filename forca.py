import random

vidas = 5
restam = 0
biblioteca = [
    'tesoura',
    'borracha',
    'caneta',
    'estojo',
    'caderno'
]
esc = ''
acertos = []
mostrando = ''


def continuar():
    global esc
    global mostrando
    global escolha
    esc = input('Continuar? [s/n] ')
    while esc not in "SsNn":
        print('Escolha S para continuar ou N para parar.')
        esc = input('continuar? [s/n]')
        if esc in 'SsNn':
            if esc in 'Nn':
                break
            elif esc in 'Ss':
                gerar()
                limpa()


def limpa():
    print('\n'*100)


def gerar():
    global escolha
    global mostrando
    global vidas
    escolha = biblioteca[random.randint(0, len(biblioteca) - 1)]
    mostrando = ''
    vidas = 5


def menu():
    global player
    global vidas
    print(f'{"":-^50}')
    print(f'Jogo da forca: {mostrando} {"Jogador: " + player: >25}')
    print(f'{"":-^50}')
    print(f'vidas: {vidas}     Restam {restam} letras')
    print(f'{"":-^50}')


gerar()
player = input('Digite seu nome: ')
while True:
    menu()
    mostrando = ''
    testeletra = False
    while not testeletra:
        letra = input('Digite uma letra: ')
        if letra.isalpha():
            testeletra = True

        if len(letra) > 1:
            print('Apenas 1 letra por tentativa')
            continue
    acertos.append(letra)
    if letra not in escolha:
        acertos.pop()
        vidas -= 1
        print(f'Errou! agora tu tens apenas {vidas} vidas.')

    for i in escolha:
        if i in acertos:
            mostrando += i
        else:
            mostrando += '*'
    limpa()

    if mostrando == escolha:
        print('Você venceu!')
        continuar()
        limpa()
    elif vidas < 1:
        print('Tu perdeu!')
        continuar()
        gerar()
        limpa()
