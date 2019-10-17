#Exercício 1: calcule a média dos numeros ímpares até 100 usando slices, a função len e a função sum

n100 = list(range(0,101))
print(f'\nListagem 0-100: {n100}')

impar = n100[1::2]
print(f'\nListagem dos números ímpares: {impar}')

imparTotal = sum(impar)
print(f'\nSomatória dos números ímpares: {imparTotal}')

media = imparTotal / len(impar)
print(f'\nMédia dos números ímpar: {media}')