# Calculadora de Consumo Elétrico Inteligente
# Versão 1.0

def calculadora_consumo():
    """
    Função principal que calcula o consumo elétrico mensal de um aparelho
    e estima o custo baseado no valor do kWh informado pelo usuário.
    """
    
    print("=" * 50)
    print("     CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE")
    print("=" * 50)
    print()
    
    # Entrada de dados do usuário
    try:
        nome_aparelho = input("Informe o nome do aparelho (ex.: Geladeira): ")
        
        potencia = float(input("Informe a potência do aparelho em watts (W): "))
        
        if potencia <= 0:
            print("❌ Erro: A potência deve ser um valor positivo!")
            return
        
        horas_dia = float(input("Informe o tempo médio de uso diário em horas: "))
        
        if horas_dia < 0:
            print("❌ Erro: O tempo de uso deve ser um valor positivo!")
            return
        
        valor_kwh = float(input("Informe o valor do kWh em R$ (ex.: 0.75): "))
        
        if valor_kwh <= 0:
            print("❌ Erro: O valor do kWh deve ser positivo!")
            return
        
    except ValueError:
        print("❌ Erro: Por favor, digite valores numéricos válidos!")
        return
    
    # Cálculo do consumo mensal em kWh
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    
    # Cálculo do custo estimado
    custo_estimado = consumo_mensal * valor_kwh
    
    # Exibição dos resultados
    print("\n" + "=" * 50)
    print("                 RESULTADO DA ANÁLISE")
    print("=" * 50)
    print()
    print(f"📱 Aparelho: {nome_aparelho}")
    print(f"⚡ Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"💰 Custo estimado: R$ {custo_estimado:.2f}/mês")
    print()
    print("=" * 50)
    
    # Informações adicionais úteis
    print("\n📊 INFORMAÇÕES ADICIONAIS:")
    print(f"   • Potência: {potencia:.0f} W")
    print(f"   • Uso diário: {horas_dia:.1f} horas/dia")
    print(f"   • Dias no mês: 30 dias")
    print(f"   • Tarifa kWh: R$ {valor_kwh:.2f}")
    # Dica econômica baseada no consumo
    if consumo_mensal > 100:
        print("\n💡 Dica: Este aparelho tem alto consumo! Considere:")
        print("   • Substituir por um modelo mais eficiente")
        print("   • Reduzir o tempo de uso")
        print("   • Utilizar durante horários de tarifa mais baixa")
    elif consumo_mensal > 50:
        print("\n💡 Dica: Consumo moderado. Para economizar:")
        print("   • Mantenha a manutenção em dia")
        print("   • Utilize apenas quando necessário")
    else:
        print("\n💡 Dica: Bom! Este aparelho tem baixo consumo.")
        print("   • Continue com hábitos de consumo consciente")
    
    print("\n" + "=" * 50)

# Execução do programa
if __name__ == "__main__":
    while True:
        calculadora_consumo()
        
        # Pergunta se o usuário quer fazer outro cálculo
        continuar = input("\nDeseja calcular outro aparelho? (s/n): ").lower()
        if continuar != 's':
            print("\n👋 Obrigado por usar a Calculadora de Consumo Elétrico!")
            break
        print("\n" + "-" * 50 + "\n")