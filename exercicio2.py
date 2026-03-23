#Teste com estes valores:
#Teste = (52.0, 1.75)  IMC 17.0 = abaixo do peso
#        (70.0, 1.75)  IMC 22.9 = Peso normal
#        (85.0, 1.70)  IMC 29.4 = Sobrepeso
#        (110.0, 1.65) IMC 40.4 = Obesidade

def calculadora_imc(peso, altura):
    imc = peso / altura**2
    imc = round(imc, 1)
    
    if imc < 18.5:
        return "Abaixo do Peso"
    elif imc <= 24.9:
        return "Peso Normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 40.4:
        return "Obesidade"
    else:
        return "Obesidade Grave"

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

valor_imc = round(peso/altura**2, 1)


# Saída esperada:
# Peso: 70.0 kg | Altura: 1.75 m
# IMC: 22.9 - Peso normal

imc = calculadora_imc(peso, altura)
print(f'Peso: {peso} kg | Altura: {altura} m')
print(f'IMC: {valor_imc} - {imc}')
