peso = float(input("Informe o peso do saco de racao em gramas: "))
quant = float(input("Informe a quantidade diaria de racao em gramas: "))
total = peso-(quant*5)
print(round(total,2))