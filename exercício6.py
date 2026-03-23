#Calculando ano bissexto
def ano_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

#Montando calendário
def dias_do_mes(mes,ano):
    if mes in [1,3,5,7,8,10,12]:
        return 31
    elif mes in [4,6,9,11]:
        return 30
    elif mes == 2:
        if ano_bissexto(ano):
            return 29
        else:
            return 28

#Nomes dos meses
def nome_mes(mes):
    meses = {1: "janeiro", 2: "fevereiro", 3:"março", 4:"abril", 5:"maio", 6:"junho", 7:"julho", 8:"agosto", 9:'setembro', 10:"outubro",11:'novembro', 12:"dezembro"}
    return meses[mes]

#Rodando o programa
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input('Digite o ano: '))

#Validando ano bissesxto
bissexto = ano_bissexto(ano)

print(f"Data: {dia:02d}/{mes:02d}/{ano}")
print(f"Ano bissesxto: {'Sim' if bissexto else 'Não'}")

#Validando meses
if mes < 1 or mes > 12:
    print(f"Data inválida: mês {mes} não existe")

#Validando dias
elif dia < 1 or dia > dias_do_mes(mes,ano):
    maximo = dias_do_mes(mes,ano)
    print(f'Data Inválida: {nome_mes(mes)} de {ano} tem no máximo {maximo} dias')

#Validando data
else:
    print("Data Válida")

# Saída esperada:
# Data: 29/02/2024
# Ano bissexto: Sim
# Data válida!
#
# Data: 29/02/2023
# Ano bissexto: Não
# Data inválida: fevereiro de 2023 tem apenas 28 dias
