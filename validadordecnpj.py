"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""


def removcaracteres(arg):
    a = arg.split('-')
    dig = a[1]
    a.pop()
    documento = []
    for x in a[0]:
        if x.isnumeric():
            documento.append(x)
    documento = ''.join(documento)
    return documento, dig


def removcaracteres2(arg):
    dig = arg[-2:]
    print(dig)
    x = len(arg) - 2
    documento = arg[0:x:1]
    print(documento)
    return documento, dig


def digito_1(arg, ind):
    c = 0
    for x in arg:
        c += int(next(ind)) * int(x)
    c = 11 - (c % 11)
    if c > 9:
        c = 0
    return c


def digito_2(cnpj, calculo, dig):
    c = 0
    for x in cnpj:
        c += int(next(calculo)) * int(x)
    c += dig * int(next(calculo))
    c = 11 - (c % 11)
    if c > 9:
        c = 0
    return str(dig)+str(c)


while True:
    calc = iter("543298765432")
    calc2 = iter("6543298765432")
    cnpj_original = input('Digite o CNPJ: ')
    if '-' in cnpj_original:
        if len(cnpj_original) == 18:
            cnpj_original, dig_original = removcaracteres(cnpj_original)
        else:
            print('verifique os números digitados!')
            continue
            
    else:
        if len(cnpj_original) == 14:
            cnpj_original, dig_original = removcaracteres2(cnpj_original)
    dig1 = digito_1(cnpj_original, calc)
    dig2 = digito_2(cnpj_original, calc2, dig1)
    if dig2 == dig_original:
        print('CNPJ verdadeiro')
    else:
        print('CNPJ falso')
    
    continuar = input('Quer continuar? [s/n]')	
    if continuar in 'Nn':
        break
