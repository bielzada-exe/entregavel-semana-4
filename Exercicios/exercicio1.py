#Exercicio 1, criar lista de numeros
numeros = [] #lista vazia
qtd = int(input("Quantos numeros?"))
for i in range (qtd):
    n = int(input("Digite um numero: "))
    numeros.append(n) #insere no fim
print("lista:", numeros)
print("tamanhos", len(numeros))