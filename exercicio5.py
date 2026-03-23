import os
#Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Montando a calculadora de desconto
def calculadora_de_desconto(valor):
    if valor <=100:
        return 0.0
    elif valor <= 300:
        return 0.10
    elif valor <= 500:
        return 0.15
    else:
        return 0.20

# Loop para repetir o programa
while True:
    limpar_tela()

#Rodando o programa
    valor = float(input("Digite o valor das compra: R$ "))
    if valor <= 0:
        print("Valor inválido!")
    else:                         #.lower e .strip usados para evitar quebras no código em casos de erros de digitação
        vip = input("Você é Cliente VIP? (sim/não): ").lower().strip() 

    #Calculando desconto progressivo
        percentual = calculadora_de_desconto(valor)
        desconto = valor * percentual

    #Calculando desconto de cliente VIP
        if vip == "sim":
            percentual_vip = 0.05
        else:
            percentual_vip = 0.0

        desconto_vip = valor * percentual_vip

    #Valor final da compra
        valor_final = valor - desconto - desconto_vip

    #Exibindo o resultado   #.2f usado para formatar os números sempre em 2 casas decimais
        print("=== Resumo da compra ===")
        print(f"Valor original: R${valor:.2f}")
        print(f"Desconto ({int(percentual*100)}%): R${desconto:.2f}")

        if vip == "sim":
            print(f"Desconto VIP (5%): R${desconto_vip:.2f}")

        print(f"Valor Final : R${valor_final:.2f}")

# Pergunta se quer continuar
    continuar = input("Nova consulta? (sim/não): ").lower().strip()
    if continuar != "sim":
        limpar_tela()
        print("VLW FLW!!!")
        break

# Teste com estes valores:
#    (80.00,  "nao"),  # Sem desconto, sem VIP
#    (200.00, "nao"),  # 10% = R$ 20.00 → R$ 180.00
#    (200.00, "sim"),  # 10% + 5% VIP = R$ 30.00 → R$ 170.00
#    (450.00, "nao"),  # 15% = R$ 67.50 → R$ 382.50
#    (1000.00, "sim"), # 20% + 5% VIP = R$ 250.00 → R$ 750.00
