#Ordenando uma lista de compra conforme a escolha do usuario e somando valor total da lista.
produtos = [
    {'Produto': 'Banana Prata', 'Qtd/Kg': 2, "Valor": 6.00},
    {'Produto': 'Farinha Mafalda', 'Qtd/Kg': 2, "Valor": 8.79},
    {'Produto': 'Vinagre', 'Qtd/Kg': 1, "Valor": 2.35},
    {'Produto': 'Massa Italiana', 'Qtd/Kg': 2, "Valor": 3.29},
    {'Produto': 'Batata', 'Qtd/Kg': 2, "Valor": 9.19},
    {'Produto': 'Catchup', 'Qtd/Kg': 1, "Valor": 6.50},
    {'Produto': 'Maionese', 'Qtd/Kg': 1, "Valor": 4.98},
    {'Produto': 'Salsicha', 'Qtd/Kg': 2, "Valor": 9.49},
]


def total(arg):
    total = sum([item['Valor'] for item in arg])
    return total


programa = True
while programa:
    ordem = input('''
    Digite [1] para ordenar de forma crescente a lista pelo produto .
    Digite [2] para ordenar de forma decrescente a lista pelo produto.
    Digite [3] para ordenar de forma crescente a lista pelo valor .
    Digite [4] para ordenar de forma decrescente a lista pelo valor.
    Digite [5] para sair.
    ''')
    if ordem == '1':
        produtos.sort(key=lambda item: item['Produto'])
    elif ordem == '2':
        produtos.sort(key=lambda item: item['Produto'], reverse=True)
    elif ordem == '3':
        produtos.sort(key=lambda item: item['Valor'])
    elif ordem == '4':
        produtos.sort(key=lambda item: item['Valor'], reverse=True)
    elif ordem == '5':
        programa = False
        continue
    else:
        print('Opção inválida! Digite apenas as opções do menu.')
    for i in produtos:
        print(f'Produto:{i["Produto"]:17} | Quantidade/Kilo: {i["Qtd/Kg"]:2} | Valor: {i["Valor"]:7}')

    print(f'total: {total(produtos):.2f}')
    teste = True
    while teste:
        r = input('Quer continuar? [s/n] ')
        if r in 'Ss':
            print('\n'*100)
            teste = False
        elif r in 'Nn':
            teste = False
            programa = False
            break
        else:
            print('Opção inválida, digite S ou N')
