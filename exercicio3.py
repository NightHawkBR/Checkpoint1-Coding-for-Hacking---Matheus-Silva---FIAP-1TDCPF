def conversor_de_moedas(valor, moeda_origem, moeda_destino):
    
    #cotações em relacão ao real no exercício
    cotacoes = {"real" : 1.00,
                "dolar": 5.15, 
                "euro": 5.55,
                "libra": 6.45,}
    
    #condições para caso for digitado uma moeda fora da tabela de cotação e números negativos
    if moeda_origem not in cotacoes or moeda_destino not in cotacoes:
        return "Opção inválida!"
    elif valor <= 0:
        return "Valor Inválido"
    
    #Convertendo os valores para real primeiro, depois para a moeda de destino
    valor_em_real = valor * cotacoes[moeda_origem]
    valor_convertido = valor_em_real / cotacoes[moeda_destino]
    return round(valor_convertido, 2)

#Testando o Conversor
valor = float(input("Digite o valor: "))    #.lower e .strip usados para evitar quebras no código em casos de erros de digitação
origem = input("Moeda de origem: ").lower().strip()
destino = input("moeda de destino: ").lower().strip()

resultado = conversor_de_moedas(valor, origem, destino)
print("O valor convertido é:"f"\n {valor} {origem} = {resultado} {destino}")

