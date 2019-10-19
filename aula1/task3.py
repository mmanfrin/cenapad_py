#Exercício 3: Gere uma lista dos números divisíveis por 3 menores que 100 em ordem reversa

div3 = list(range(3,101,3))

print(f'\nLista de divisíveis por 3: {div3}')

div3.reverse()

print(f'\nLista invertida: {div3}')