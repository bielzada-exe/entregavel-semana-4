#Exercicio 3: ordenar a lista
texto = input("Numeros separados por espaco: ")
numeros = [int(x) for x in texto.split()]
numeros.sort()  #ordem crescente
print("Crescente:", numeros)
#Copia ordenada ao contrario
print("Descrente: ", sorted(numeros, reverse=True))