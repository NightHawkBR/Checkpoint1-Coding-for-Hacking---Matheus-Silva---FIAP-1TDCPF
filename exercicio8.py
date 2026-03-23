#Calculado hora de entrada e saída
def calcular_horas(entrada,saida):
    if saida > entrada:
        return saida - entrada
    else:
        return (24 - entrada) + saida

#Calculando valor por hora
def calcular_valor_base(horas):
    if horas <= 1:
        return 10.00
    else:
        return 10.00 + (horas-1)*5.00

#Verificando adicional noturno
def tem_adicional_noturno(entrada,saida):
    if entrada >= 22 or entrada < 6:
        return True
    elif saida >22 or saida <= 6:
        return True
    else:
        return False

#Verificando desconto de placa par na segunda
def tem_desconto_placa(placa,dia):
    if dia == "segunda" and placa % 2 == 0:
        return True
    else:
        return False

#Rodando o programa
entrada = int(input("Hora de entrada (0-23): "))
saida   = int(input("Hora de saída   (0-23): "))
placa   = int(input("Último número da placa: "))
dia     = input("Dia da semana: ").lower().strip()

# Validações
if entrada < 0 or entrada > 23:
    print("Hora de entrada inválida!")
elif saida < 0 or saida > 23:
    print("Hora de saída inválida!")
elif entrada == saida:
    print("Menos de 1 hora: R$10.00 (mínimo)")
elif placa < 0 or placa > 9:
    print("Último número da placa inválido! Digite um número de 0 a 9.")
else:
    # Cálculos
    horas      = calcular_horas(entrada,saida)
    valor_base = calcular_valor_base(horas)

    adicional_noturno = 0.0
    desconto_placa    = 0.0

    if tem_adicional_noturno(entrada,saida):
        adicional_noturno = valor_base*0.50

    total_parcial = valor_base + adicional_noturno

    if tem_desconto_placa(placa, dia):
        desconto_placa = total_parcial*0.10

    total = total_parcial - desconto_placa

    #Exibindo o resultado
    print(f"\n=== Estacionamento ===")
    print(f"Entrada:{entrada}h | Saída:{saida}h")
    print(f"Tempo:{horas} hora(s)")
    print(f"Valor base:               R$ {valor_base:.2f}")

    if tem_adicional_noturno(entrada, saida):
        print(f"Adicional noturno (50%):  R$ {adicional_noturno:.2f}")

    if tem_desconto_placa(placa, dia):
        print(f"Desconto placa par (10%): R$ {desconto_placa:.2f}")

    print(f"Total:                    R$ {total:.2f}")
