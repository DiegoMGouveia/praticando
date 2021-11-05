cpf = input('digite seu cpf: [000.000.000-00]


def limpastrings(args):
    args = str(args)
    a, b = args.split('-')
    a = a.split('.')
    a = ''.join(a)
    return a, b


def calculo(args):
    args = list(args)
    args2 = str(args[1]) #digito
    args = str(args[0])
    a = 10
    soma = 0
    soma2 = 0
    for i in args:
        soma += int(i) * a
        a -= 1
    soma = 11-(soma%11)
    if soma > 9:
        soma = 0
    a = 11
    for i in args:
        soma2 += int(i) * a
        a -= 1
    soma2 += soma*a
    soma2 = 11-(soma2%11)
    soma = str(soma)
    if soma2 > 9:
        soma2 = str(0)
    else:
        soma2 = str(soma2)
    soma += soma2
    if soma == args2:
        soma = 'CPF VÁLIDO!'
    else:
        soma = 'CPF INVÁLIDO'
    return soma

t = calculo(limpastrings(cpf))
print(t)
