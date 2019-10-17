# Exercício 1
# Faça um joguinho de "Advinhe o número". Baseie-se no exemplo e modifique-o para:
# 1- Informar ao jogador o número de tentativas até então
# 2- A cada tentativa, dizer ao jogador o intervalo em que se encontra o número. Por exemplo: "O número está entre 1 e 100". "O número está entre 70 e 100". "O número está entre 70 e 85" etc.
# 3- No final informe: "Você acertou com X tentativas"

import os
import random
n = random.randint(1, 101) #Número aleatório de 1 a 100
#n = 50
os.system("cls")
#os.system("clear")

print("Adivinhe o número!\n**********")
print(n)
guess = int(input("Entre com um número de 1 a 100: "))
while n != guess:
    if guess < n:
        print("guess is low")
        guess = int(input("Entre com um número de 1 a 100:: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Entre com um número de 1 a 100:: "))
    else:
        print("you guessed it!")
        break
print("you guessed it!")


#BKP
# import random
# n = random.randint(1, 101) #Número aleatório de 1 a 100
# guess = int(input("Entre com um número de 1 a 100:: "))
# while n != guess:
#     if guess < n:
#         print("guess is low")
#         guess = int(input("Entre com um número de 1 a 100:: "))
#     elif guess > n:
#         print("guess is high")
#         guess = int(input("Entre com um número de 1 a 100:: "))
#     else:
#         print("you guessed it!")
#         break