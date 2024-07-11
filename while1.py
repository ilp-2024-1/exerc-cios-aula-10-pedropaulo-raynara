#questão 1
num = 1
while num <= 100:
    print(num)
    num += 1 
print("Programa encerrado.")

#questão 2 
num = 1 
soma = 0
while num != 0:
    num = int(input("insira valores:"))
    soma = soma + num
    if num == 0:
        print("a soma do valores é:", soma)
print("fim do programa")

#questão 3 
senha = 1234
login = int(input("digite a senha:"))
while login != senha:
  print("senha incorreta")
  login = int(input("digite a senha:"))

print("senha correta!!!")
print("fim do programa")

#questão 4 
import random 
random_num = random.randint(1,100)
tentativas = 0 
palpite = int(input("chute um número (entr 1 e 100):"))
while palpite != random_num:
    print("número incorreto")
    palpite = int(input("chute um número (entr 1 e 100):"))
    tentativas +=1
if palpite == random_num:
    print(f"Parabéns! você acertou o número secreto {random_num} em {tentativas} tentativas.")
print("fim do programa")

#questão 5
num_int= int(input("digite um número inteiro e positivo:"))
contador = 1
fatorial = 1
while num_int <= 0:
    print("este não é um número inteiro positivo")
    num_int = int(input("digite um número inteiro e positivo:"))
while contador <= num_int:
    fatorial *= contador
    contador += 1 
print(f"o fatorial de {num_int} é {fatorial}")
print("fim do programa.")







