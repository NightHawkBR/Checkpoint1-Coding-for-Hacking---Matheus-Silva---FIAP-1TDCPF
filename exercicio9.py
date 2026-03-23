import random

#Dicionário de opções
opcoes = {
    1: "Pedra",
    2: "Papel",
    3: "Tesoura",
    4: "Lagarto",
    5: "Spock"
}

#Regras — quem vence quem e o motivo
regras = {
    ("Tesoura", "Papel")  : "Tesoura corta Papel",
    ("Papel",   "Pedra")  : "Papel cobre Pedra",
    ("Pedra",   "Lagarto"): "Pedra esmaga Lagarto",
    ("Lagarto", "Spock")  : "Lagarto envenena Spock",
    ("Spock",   "Tesoura"): "Spock derrete Tesoura",
    ("Tesoura", "Lagarto"): "Tesoura decapita Lagarto",
    ("Lagarto", "Papel")  : "Lagarto come Papel",
    ("Papel",   "Spock")  : "Papel refuta Spock",
    ("Spock",   "Pedra")  : "Spock vaporiza Pedra",
    ("Pedra",   "Tesoura"): "Pedra quebra Tesoura",
}

#Função que decide o resultado
def verificar_resultado(jogador, computador):
    if jogador == computador:
        return "empate", "Empate! "
    elif (jogador, computador) in regras:
        motivo = regras[(jogador, computador)]
        return "vitoria", f"{motivo} — Você ganhou! "
    else:
        motivo = regras[(computador, jogador)]
        return "derrota", f"{motivo} — Você perdeu! "

#Programa principal

print(" 1 - Pedra")
print(" 2 - Papel")
print(" 3 - Tesoura")
print(" 4 - Lagarto")
print(" 5 - Spock")


escolha = int(input("Escolha uma opção (1-5): "))

# Validação
if escolha < 1 or escolha > 5:
    print("Opção inválida! Escolha entre 1 e 5.")
else:
    jogador    = opcoes[escolha]
    computador = opcoes[random.randint(1, 5)]

    resultado, mensagem = verificar_resultado(jogador, computador)

    print(f"\n  Você escolheu:       {jogador}")
    print(f"  Computador escolheu: {computador}")
    print(f"\n  {mensagem}")
