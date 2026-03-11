peso_saco = float(input("peso do saco de racao em gramas"))
quant_diaria = float(input("quantidade diaria de racao em gramas"))
quant_semanal = 7  +  quant_diaria
restante = peso_saco - quant_semanal
print(round(restante, 2))