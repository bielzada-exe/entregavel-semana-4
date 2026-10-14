programa
{
    funcao inicio()
    {
        inteiro quantidade
        cadeia nomes[100]
        cadeia categorias[100]
        real precos[100]

        real valor_filtro
        cadeia tipo_filtro

        escreva("Quantos produtos deseja cadastrar? ")
        leia(quantidade)

        // Cadastro dos produtos
        para (inteiro i = 0; i < quantidade; i++)
        {
            escreva("\nProduto ", i + 1, "\n")

            escreva("Nome: ")
            leia(nomes[i])

            escreva("Preço: R$ ")
            leia(precos[i])

            escreva("Categoria: ")
            leia(categorias[i])
        }

        // Filtro por preço
        escreva("\nDigite um valor para filtrar: R$ ")
        leia(valor_filtro)

        escreva("Digite 'acima' ou 'abaixo': ")
        leia(tipo_filtro)

        escreva("\n=== PRODUTOS FILTRADOS ===\n")

        para (inteiro i = 0; i < quantidade; i++)
        {
            se (tipo_filtro == "acima" e precos[i] > valor_filtro)
            {
                escreva(
                    nomes[i],
                    " | R$ ",
                    precos[i],
                    " | ",
                    categorias[i],
                    "\n"
                )
            }

            se (tipo_filtro == "abaixo" e precos[i] < valor_filtro)
            {
                escreva(
                    nomes[i],
                    " | R$ ",
                    precos[i],
                    " | ",
                    categorias[i],
                    "\n"
                )
            }
        }

        // Estatísticas
        real menor_preco = precos[0]
        real maior_preco = precos[0]
        real soma_precos = 0
        real media_preco

        para (inteiro i = 0; i < quantidade; i++)
        {
            soma_precos = soma_precos + precos[i]

            se (precos[i] < menor_preco)
            {
                menor_preco = precos[i]
            }

            se (precos[i] > maior_preco)
            {
                maior_preco = precos[i]
            }
        }

        media_preco = soma_precos / quantidade

        escreva("\n=== ESTATÍSTICAS GERAIS ===\n")
        escreva("Menor preço: R$ ", menor_preco, "\n")
        escreva("Maior preço: R$ ", maior_preco, "\n")
        escreva("Média dos preços: R$ ", media_preco, "\n")
    }
}