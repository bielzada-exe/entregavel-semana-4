produtos = [
    {"nome": "Notebook", "preco": 3500.00, "categoria": "Eletrônicos"},
    {"nome": "Mouse", "preco": 80.00, "categoria": "Acessórios"},
    {"nome": "Teclado", "preco": 150.00, "categoria": "Acessórios"},
    {"nome": "Monitor", "preco": 1200.00, "categoria": "Eletrônicos"},
    {"nome": "Cadeira Gamer", "preco": 900.00, "categoria": "Móveis"},
    {"nome": "Headset", "preco": 250.00, "categoria": "Acessórios"},
]

valor_filtro = float(input("Digite o valor para filtrar os produtos: ")) #Valor de filtro para os produtos

tipo_filtro = input("Digite 'acima' ou 'abaixo': ").strip().lower() #tipo de filtro

if tipo_filtro == "acima":
    produtos_filtrados = [
        produto for produto in produtos
        if produto["preco"] > valor_filtro
    ]
elif tipo_filtro == "abaixo":
    produtos_filtrados = [
        produto for produto in produtos
        if produto["preco"] < valor_filtro
    ]
else:
    produtos_filtrados = []
    print("Opção de filtro inválida.")

produtos_crescente = sorted(produtos, key=lambda produto: produto["preco"]) #Organizar os produtos em ordem crescente de preço

produtos_decrescente = sorted(produtos, key=lambda produto: produto["preco"], reverse=True) #Organizar os produtos em ordem decrescente de preço

categorias = {produto["categoria"] for produto in produtos}#Categoria dos produtos, usando set para não ter duplicatas

precos = [produto["preco"] for produto in produtos]

#organizando os preços para calcular estatísticas
menor_preco = min(precos)
maior_preco = max(precos)
media_preco = sum(precos) / len(precos) #Calcula a média dos preços dos produtos

estatisticas = (menor_preco, maior_preco, media_preco)

# ==================================================
# RELATÓRIO FINAL
# ==================================================

print("\n" + "=" * 50)
print("RELATÓRIO DE PRODUTOS")
print("=" * 50)

print(f"\nValor utilizado no filtro: R$ {valor_filtro:.2f}")
print(f"Tipo de filtro: {tipo_filtro}")

print("\n--- PRODUTOS FILTRADOS ---")

if produtos_filtrados:
    for produto in produtos_filtrados:
        print(
            f"- {produto['nome']} | "
            f"R$ {produto['preco']:.2f} | "
            f"{produto['categoria']}"
        )
else:
    print("Nenhum produto encontrado.")

print("\n--- PREÇOS CRESCENTES ---")

for produto in produtos_crescente:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

print("\n--- PREÇOS DECRESCENTES ---")

for produto in produtos_decrescente:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

print("\n--- CATEGORIAS ---")

for categoria in sorted(categorias):
    print(f"- {categoria}")

print("\n--- ESTATÍSTICAS ---")

print(f"Menor preço: R$ {estatisticas[0]:.2f}")
print(f"Maior preço: R$ {estatisticas[1]:.2f}")
print(f"Média dos preços: R$ {estatisticas[2]:.2f}")

print("\n" + "=" * 50)
print("FIM DO RELATÓRIO")
print("=" * 50)