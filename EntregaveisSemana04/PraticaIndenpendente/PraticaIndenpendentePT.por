programa
{
    funcao inicio()
    {
        cadeia nomes[100]
        cadeia temporario
        cadeia primeiro
        cadeia ultimo

        inteiro quantidade = 0
        inteiro i, j
        logico repetido

        // 1. Entrada dos nomes
        enquanto (quantidade < 100)
        {
            escreva("Digite um nome (ou 'fim' para finalizar): ")
            leia(nomes[quantidade])

            se (nomes[quantidade] == "fim")
            {
                pare
            }

            quantidade++
        }

        // 2. Remover nomes repetidos
        i = 0

        enquanto (i < quantidade)
        {
            repetido = falso
            j = i + 1

            enquanto (j < quantidade)
            {
                se (nomes[i] == nomes[j])
                {
                    repetido = verdadeiro

                    // Desloca os elementos para a esquerda
                    enquanto (j < quantidade - 1)
                    {
                        nomes[j] = nomes[j + 1]
                        j++
                    }

                    quantidade--
                }
                senao
                {
                    j++
                }
            }

            i++
        }

        // 3. Ordenação pelo método da bolha
        para (i = 0; i < quantidade - 1; i++)
        {
            para (j = 0; j < quantidade - i - 1; j++)
            {
                se (nomes[j] > nomes[j + 1])
                {
                    temporario = nomes[j]
                    nomes[j] = nomes[j + 1]
                    nomes[j + 1] = temporario
                }
            }
        }

        // 4. Primeiro e último nome
        primeiro = nomes[0]
        ultimo = nomes[quantidade - 1]

        // 5. Relatório
        escreva("\n===== RELATÓRIO FINAL =====\n")
        escreva("Quantidade de nomes únicos: ", quantidade, "\n")

        escreva("Lista ordenada: ")

        para (i = 0; i < quantidade; i++)
        {
            escreva(nomes[i])

            se (i < quantidade - 1)
            {
                escreva(", ")
            }
        }

        escreva("\n")
        escreva("Primeiro nome: ", primeiro, "\n")
        escreva("Último nome: ", ultimo, "\n")
    }
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 2240; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */