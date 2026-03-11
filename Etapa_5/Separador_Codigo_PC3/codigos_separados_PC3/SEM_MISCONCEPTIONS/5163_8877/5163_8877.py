peso_saco = float(input("Digite o peso do saco (g): "))
quant_saco = float(input("Digite a quantidade diaria utilizada (g): "))

restante = peso_saco - (quant_saco * 5)

print(float(round(restante,3)))