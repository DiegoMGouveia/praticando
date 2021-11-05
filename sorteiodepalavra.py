#criei esse sisteminha de palavras aleatórias dentro de dicionários
#afim de praticar o uso de funções e dicionários

from random import randint

biblioteca = {
    'comida': {
        1: 'Banana',
        2: 'Guisado',
        3: 'arroz',
        4: 'espinafre',
        5: 'Feijão',
        6: 'Panqueca',
    },
    'bebida': {
        1: 'Leite',
        2: 'Café',
        3: 'Chá',
        4: 'Refrigerante',
        5: 'Chimarrão',
        6: 'Suco',
    },
}
categoria = list(biblioteca)


def sortear(args):
    palavra = args[randint(1, 6)]
    return palavra


categoria_escolhida = input(f'Escolha  uma categoria {categoria}: ')
palavra = sortear(biblioteca[categoria_escolhida])
print(f'Categoria escolhida: {categoria_escolhida}\n '
      f'Palavra sorteada: {palavra}')
