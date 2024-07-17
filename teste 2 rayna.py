print('soma da série')
n = int(input('digite um número inteiro:'))
soma = 0
serie = 1

while serie <= n:
    soma += 1/serie
    serie += 1
print(f'a soma da série harmônica até o enésimo termo({n}) é {soma}:')
print('fim do programa')