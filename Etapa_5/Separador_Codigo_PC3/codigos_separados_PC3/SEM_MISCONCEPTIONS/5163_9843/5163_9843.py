peso = float(input("Digite o valor do peso da racao para gatos: "))
quant = float(input("Digite a quantidade diaria de racao fornecida aos gatos: "))

valor = peso - (5 * quant)

print(round(valor, 3))