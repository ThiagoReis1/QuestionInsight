consumo = float(input())
totalPlano = (0.28 * consumo) + 23
totalAPagar = totalPlano + totalPlano * 31/100
print(round(totalAPagar,2))