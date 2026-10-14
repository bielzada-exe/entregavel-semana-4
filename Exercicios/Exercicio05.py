#Exercicio 5: tuplas de estatisticas
texto = input("Notas separadas por espaco: ")
notas = [float(x) for x in texto.split()]
#tuplas e imutavel: protege  resultado
estat = (min(notas), max(notas), sum(notas) / len(notas))
print("Minimo:", estat[0])
print("Maximo:", estat[1])
print("Media: %.2f" % estat[2])