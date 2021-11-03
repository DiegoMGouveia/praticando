cpf = input('Digite um cpf: [000.000.000-00')
cpf_original = cpf
soma = 0
soma2 = 0
t = 10
cpf = cpf.split('-')
digitos = cpf[1]
cpf.pop()
cpf = str(cpf)
for i in cpf:
    if i in '1234567890':
        while t:
            soma += int(i)*t
            t -= 1
            break
num1 = 11 - (soma % 11)
num3 = num1
if num1 > 9:
    num1 = str(0)
t = 10
t += 1
for i in cpf:
    if i in '1234567890':
        while t:
            soma2 += int(i)*t
            t -= 1
            break
soma2 += num3 * t
num2 = 11 - (soma2 % 11)
if num2 > 9:
    num2 = str(0)
num3 = str(num1)+str(num2)
digitos2 = num3
if digitos == digitos2:
    print(f'O CPF {cpf_original} é um cpf valido!')
else:
    print(f'O CPF {cpf_original} é um cpf inválido!')