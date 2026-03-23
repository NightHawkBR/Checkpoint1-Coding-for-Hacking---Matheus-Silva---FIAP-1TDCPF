#Definindo o que é um triângulo 
def triangulo_valido(a,b,c):
        if a + b > c and b + c > a and a + c > b:
            return True
        else:
            return False

#Definindo tipos de triângulo
def classificar_lados(a,b,c):
        if a == b == c:
            return "Equilátero"
        elif a == b or b == c or a == c:
            return "Isóceles"
        else:
            return "Escaleno"

#Rodando o programa
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

if not triangulo_valido(a,b,c):
    print("Esses lados não formam um triângulo")
else:
     lados = classificar_lados(a,b,c)
     #Mostrando os lados em números inteiros
     print(f"Lados: {int(a)},{int(b)},{int(c)}")
     print(f"Tipo de Triângulo: {lados}") 
     print(f"Triângulo válido")

# Teste com estes valores:
#    (5, 5, 5),    # Equilátero
#    (5, 5, 3),    # Isósceles
#    (3, 4, 5),    # Escaleno
#    (1, 2, 10),   # Não forma triângulo (1 + 2 < 10)
#    (0, 5, 5),    # Não forma triângulo (lado zero)
#    (7, 7, 12),   # Isósceles
