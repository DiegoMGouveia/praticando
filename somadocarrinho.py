#Neste codigo, irei somar o valor que esta dentro de um carrinho e-commerce
#exercicio 73 do curso
carrinho = []
carrinho.append(('Produto 1', 50.30))
carrinho.append(('Produto 2', 10))
carrinho.append(('Produto 3', 60))
total = sum([i[1] for i in carrinho])
print('total:',total)
