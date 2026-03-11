peso = float(input("Digite o peso do saco de racao: "))

quant_diaria = float(input("Digite a quantidade diaria de racao: "))

quant_total = peso - (quant_diaria * 4)

print(round(quant_total, 2))