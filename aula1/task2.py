#Exercício 2 - aula 1
#retorne o último sobrenome da string nome

#nome = "Fulano da Silva"

#Recebendo o nome
print('Digite seu nome: ')
nome = input()

#separando caracterres separados por espaço
nomeSep = nome.split(sep=' ')

#identificando o último sobrenome
ultNome = nomeSep[-1]

print('Último sobrenome é: ' + ultNome)