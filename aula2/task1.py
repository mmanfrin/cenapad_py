# Exercício 1
# Faça um joguinho de "Advinhe o número". Baseie-se no exemplo e modifique-o para:
# 1- Informar ao jogador o número de tentativas até então
# 2- A cada tentativa, dizer ao jogador o intervalo em que se encontra o número. Por exemplo: "O número está entre 1 e 100". "O número está entre 70 e 100". "O número está entre 70 e 85" etc.
# 3- No final informe: "Você acertou com X tentativas"


import os
import random

os.system('cls')

#n = int(5)
n = random.randint(1,100)
#print(n)

#guess = int(5)
guess = int(input('Tente adivinhar o X. Insira seu palpite entre 1 e 100: '))
x = 1
menor = 1
maior = 100


while guess != n:
    if guess < n:
        x += 1
        menor = int(guess)
        print('\nSeu palpite é MENOR que X.')
        guess = int(input(f'Insira outro número entre {menor} e {maior}: '))
        x += 1
        #print(x)
    elif guess > n:
        x += 1
        maior = int(guess)
        print('\nSeu palpite é MAIOR que X.')
        guess = int(input(f'Insira outro número entre {menor} e {maior}: '))
        #print(x)
    else:
        break


os.system('cls')
print(f'\nVocê acertou em {x} tentativa(s)!\nO valor de X é {n}.')