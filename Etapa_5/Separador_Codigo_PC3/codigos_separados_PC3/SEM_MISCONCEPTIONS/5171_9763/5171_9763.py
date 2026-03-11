peso = float(input("informe o peso do saco de racao: "))
quant_diaria = float(input("informe a quantidade em gramas: "))

final = peso-(quant_diaria*7)

print(round(final, 2))