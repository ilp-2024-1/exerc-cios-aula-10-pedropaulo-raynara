print('calcule a soma dos dígitos')
n = int(input('digite um numero inteiro:'))
soma = 0
num = abs (n)

while num > 0:
    digito = num % 10
    soma += digito
    num //= 10

print(f'entrada: {n} saída: {soma}')
print('fim do programa')