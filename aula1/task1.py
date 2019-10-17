#Exercício 1, aula 1
#calcule a média dos numeros ímpares até 100 usando slices, a função len e a função sum

#gerando lista de 0 a 100
numeros_ate_100 = list(range(0,101))
#print(numeros_ate_100)

#selecionando os números impares / contagem dos números da lista
numeros_impares = numeros_ate_100[1::2]
total_impar = len(numeros_impares)
#print(numeros_impares)
#print(total_impar)

#calculando a somatória e a média
soma = sum(numeros_impares)
media = soma / total_impar

#print("Média é igual a: " + int(media)
print("Média é igual a:")
print(media)