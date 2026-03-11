kWh = float(input(" Imforme a quantidade de kWh:"))
valorTotal = kWh * 0.43 + 10
icms = valorTotal * 25/100
valorTotal = valorTotal + icms
print(round(valorTotal,2))