from random import randint
j = 10
soma = 0
cpf = randint(100000000, 999999999)
print(cpf)
cpf = str(cpf)
for i in cpf:
    while j:
        soma += int(i) * j
        j -= 1
        break

digito1 = 11 - (soma % 11)
if digito1 > 9:
    digito1 = 0
soma = 0
j = 11
for i in cpf:
    while j:
        soma += int(i) * j
        j -= 1
        break
soma += digito1 * j
digito2 = 11 - (soma % 11)
if digito2 > 9:
    digito2 = 0
cpf = str(cpf)
cpf += str(digito1)
cpf += str(digito2)
print(cpf)