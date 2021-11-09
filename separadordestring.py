#exercicio dobre list comprehentions
#exercicio do curso, separar a string em 9 caracteres e depois juntar por pontos.
lista = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10 #quantidade de caracteres para separar
a = [lista[i:i + n] for i in range(0, len(lista), n)]
a = '.'.join([i for i in a])
print(a)
