# Saída esperada:
# Idade 5   → Criança
# Idade 15  → Adolescente
# Idade 25  → Adulto
# Idade 70  → Idoso
# Idade -3  → Idade inválida
# Idade 150 → Idade inválida

#1 pedir a idade do usuário
def definidor_de_idade(idade_em_anos: int, idade_em_meses: int = 0):
    if idade_em_anos < 0 or idade_em_anos > 120:
        return "Idade inválida"
    elif idade_em_anos == 0:
        if idade_em_meses < 12:
            return "Recém-nascido"
    elif idade_em_anos <= 2:
        return "Bebê"
    elif idade_em_anos <= 11:
        return "Criança"
    elif idade_em_anos <= 17:
        return "Adolescente"
    elif idade_em_anos <= 59:
        return "Adulto"
    else:
        return "Idoso"

print("qual a sua idade em anos?")
idade_anos = int(input())
print("qual sua idade em meses?")
idade_meses = int(input())

print("Você é:", definidor_de_idade (idade_anos, idade_meses))
