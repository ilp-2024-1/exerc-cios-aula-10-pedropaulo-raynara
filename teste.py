print('sequência de fibonacci')
n = int(input('digite um numero inteiro positivo:'))
n1 = 0
n2 = 1
print('{} {}'. format (n1, n2), end=' ')
count = 3
while count <= n:
    n3 = n1 + n2
    print('{}'. format (n3), end=' ')
    n1 = n2
    n2 = n3
    count += 1  
print( '\n' 'fim do programa')