##1º bloco - função de cálculo 

def calcular_desconto(valor_compra):
    """
    Calcula o desconto progressivo com base no valor total da compra.
    
    Args:
        valor_compra (float): Valor total da compra
    
    Returns:
        tuple: (porcentagem_desconto, valor_desconto, valor_final)
    """

##sub-bloco1 - Percentual de desconto

    if valor_compra < 200:
        porcentagem = 5
    elif 200 <= valor_compra < 300:
        porcentagem = 10
    else:  # valor_compra >= 300
        porcentagem = 15

##sub-bloco2 - cálculo dos valores monetários
    
    valor_desconto = valor_compra * (porcentagem / 100)
    valor_final = valor_compra - valor_desconto

##sub-bloco3 - retorno dos resultados
    
    return porcentagem, valor_desconto, valor_final

##2º Bloco - Mensagem para o usuário

def main():
    """Função principal do programa"""

##sub-bloco1 - cabeçalho de regras

    print("=" * 50)
    print("       SISTEMA DE DESCONTO PROGRESSIVO")
    print("=" * 50)
    print("\nRegras de desconto:")
    print("- Compras até R$ 200,00: 5% de desconto")
    print("- Compras de R$ 200,01 a R$ 299,99: 10% de desconto")
    print("- Compras a partir de R$ 300,00: 15% de desconto")
    print("=" * 50)

##sub-bloco2 - validação de entrada de dados
    
    try:
        # Solicita o valor da compra ao usuário
        valor_compra = float(input("\nDigite o valor total da compra: R$ "))

##sub-bloco3 - verificação de valor negativo
        
        if valor_compra < 0:
            print("\n❌ Erro: O valor da compra não pode ser negativo!")
            return

##sub-bloco4 - função de cálculo de desconto
        
        # Calcula o desconto
        porcentagem, valor_desconto, valor_final = calcular_desconto(valor_compra)

##sub-bloco5 - exibe resultados
        
        # Exibe os resultados formatados
        print("\n" + "=" * 50)
        print("          RESULTADO DO CÁLCULO")
        print("=" * 50)
        print(f"Valor total da compra:     R$ {valor_compra:.2f}")
        print(f"Percentual de desconto:    {porcentagem}%")
        print(f"Valor do desconto:         R$ {valor_desconto:.2f}")
        print(f"Valor a pagar:             R$ {valor_final:.2f}")
        print("=" * 50)

##sub-bloco6 - dicas de economia conforme valor(escala progressiva)
        
        # Dica econômica
        if valor_compra < 200:
            print(f"\n💡 Compre mais R$ {200 - valor_compra:.2f} para ganhar 10% de desconto!")
        elif 200 <= valor_compra < 300:
            print(f"\n💡 Compre mais R$ {300 - valor_compra:.2f} para ganhar 15% de desconto!")
        else:
            print("\n🎉 Você já está na faixa de maior desconto!")

##sub-bloco7 - tratamento de erro na digitação
            
    except ValueError:
        print("\n❌ Erro: Por favor, digite um valor numérico válido!")
        print("   Use ponto (.) como separador decimal. Exemplo: 199.99")

##3º Bloco - verificação de execução

if __name__ == "__main__": ##chama a função principal
    main() ##após execução o program finaliza

