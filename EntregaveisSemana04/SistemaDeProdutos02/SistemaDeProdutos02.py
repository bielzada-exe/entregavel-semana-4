# Cadastro de produtos
produtos = []

quantidade_produtos = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade_produtos):
    print(f"\nProduto {i + 1}")

    nome = input("Nome: ")
    preco = float(input("Preço: R$ "))
    categoria = input("Categoria: ")

    produto = {
        "nome": nome,
        "preco": preco,
        "categoria": categoria
    }

    produtos.append(produto)


# Filtro por preço
valor_filtro = float(input("\nDigite um valor para filtrar: R$ "))

tipo_filtro = input(
    "Digite 'acima' para produtos acima do valor "
    "ou 'abaixo' para produtos abaixo: "
).lower()

produtos_filtrados = []

for produto in produtos:
    if tipo_filtro == "acima" and produto["preco"] > valor_filtro:
        produtos_filtrados.append(produto)

    elif tipo_filtro == "abaixo" and produto["preco"] < valor_filtro:
        produtos_filtrados.append(produto)


# Ordenação crescente
produtos_crescente = sorted(
    produtos,
    key=lambda produto: produto["preco"]
)


# Ordenação decrescente
produtos_decrescente = sorted(
    produtos,
    key=lambda produto: produto["preco"],
    reverse=True
)


# Categorias únicas usando set
categorias = set()

for produto in produtos:
    categorias.add(produto["categoria"])


# Lista somente com os preços
precos = []

for produto in produtos:
    precos.append(produto["preco"])


# Estatísticas
menor_preco = min(precos)
maior_preco = max(precos)
media_preco = sum(precos) / len(precos)

estatisticas = (menor_preco, maior_preco, media_preco)


# Relatório final
print("\n" + "=" * 50)
print("RELATÓRIO FINAL")
print("=" * 50)

print(f"\nQuantidade de produtos: {len(produtos)}")

print(f"\nProdutos filtrados ({tipo_filtro} R$ {valor_filtro:.2f}):")

if produtos_filtrados:
    for produto in produtos_filtrados:
        print(
            f"- {produto['nome']} | "
            f"R$ {produto['preco']:.2f} | "
            f"{produto['categoria']}"
        )
else:
    print("Nenhum produto encontrado.")


print("\nProdutos por preço crescente:")

for produto in produtos_crescente:
    print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")


print("\nProdutos por preço decrescente:")

for produto in produtos_decrescente:
    print(f"- {produto['nome']}: R$ {produto['preco']:.2f}")


print("\nCategorias únicas:")

for categoria in sorted(categorias):
    print(f"- {categoria}")


print("\nEstatísticas gerais:")
print(f"Menor preço: R$ {estatisticas[0]:.2f}")
print(f"Maior preço: R$ {estatisticas[1]:.2f}")
print(f"Média dos preços: R$ {estatisticas[2]:.2f}")

print("\n" + "=" * 50)