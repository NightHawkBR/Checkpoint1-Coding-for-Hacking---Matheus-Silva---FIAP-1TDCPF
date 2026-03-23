#Calculando a quantidade de notas necessárias
def calcular_cedulas(valor):
    c200 = valor//200
    valor -= c200*200

    c100 = valor//100
    valor -= c100*100

    c50 = valor//50
    valor -= c50*50

    c20 = valor//20
    valor -= c20*20

    c10 = valor//10
    valor -= c10*10

    return c200,c100,c50,c20,c10

#Rodando o programa
valor = int(input("Digite o valor do saque: R$ "))

#Validando valores
if valor <=0:
    print("Valor Inválido!")
elif valor % 10 != 0:
    print ("Valor Inválido! Digite um valor de saque múltiplo de r$10")
else:
    c200,c100,c50,c20,c10 = calcular_cedulas(valor)

    #Calculando o número de cédulas
    total_cedulas = c200+c100+c50+c20+c10

    print(f"=== Saque: R$ {valor} ===")
    
    if c200 > 0:
        print(f"R$ 200: {c200} cédula(s)")
    if c100 > 0:
        print(f"R$ 100: {c100} cédula(s)")
    if c50 > 0:
        print(f"R$ 50:  {c50} cédula(s)")
    if c20 > 0:
        print(f"R$ 20:  {c20} cédula(s)")
    if c10 > 0:
        print(f"R$ 10:  {c10} cédula(s)")

    print(f"Total de cédulas: {total_cedulas}")

# Saída esperada (saque R$ 380):
# === Saque: R$ 380 ===
# R$ 200: 1 cédula(s)
# R$ 100: 1 cédula(s)
# R$ 50:  1 cédula(s)
# R$ 20:  1 cédula(s)
# R$ 10:  1 cédula(s)
# Total de cédulas: 5
