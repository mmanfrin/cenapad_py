#!/usr/bin/env python

import os
import random
os.system('cls')
i = 1 #contador
n = random.randint(1, 101) #Número aleatório de 1 a 100
#guess = int(input('Insira um número de 0 a 100: '))
guess = [int(input('Insira um número de 0 a 100: '))]
print('N = ' + str(n))

while n != guess:
    print()
    if n < guess:
        os.system('cls')
        guess = int(input('Tentativa ' + str(i) + '. Número ' + str(guess) + ' é maior que N.\n\nTente outro número de 0 a 100: '))
    elif n > guess:
        os.system('cls')
        guess = int(input('Tentativa ' + str(i) + '. Número ' + str(guess) + ' é menor que N.\n\nTente outro número de 0 a 100: '))
    else:
        break
    i += 1
os.system('cls')
print('Você acertou o número -> ' + str(n))
print('Número de tentativas: ' + str(i))
