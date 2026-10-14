nomes = [] #Onde os nomes digitados serão guardados

while True:
    nome = input("Digite um nome (ou pressione Enter para finalizar): ") #Vai pedir para o usuário digitar um nome, e se ele apertar Enter sem digitar nada, o loop vai parar

    if nome == "":
        break

    nomes.append(nome) #Append vai adicionar o nome digitado na lista de nomes

nomes_sem_duplicatas = set(nomes) #Set vai remover os nomes duplicados da lista de nomes

nomes_ordenados = sorted(nomes_sem_duplicatas) #vai ordenar os nomes

print("\nLista final:")
for nome in nomes_ordenados:
    print(nome) #Vai mostrar o resultado.