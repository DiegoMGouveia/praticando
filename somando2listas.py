lista_1 = [1, 2, 3, 4, 5, 6]
lista_2 = [1, 2, 3, 4]
total = zip(lista_1, lista_2)
for i in total:
    print(i[0]+i[1])
