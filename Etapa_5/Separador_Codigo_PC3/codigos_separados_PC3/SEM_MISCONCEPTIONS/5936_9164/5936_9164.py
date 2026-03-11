kWh = float(input("Digite quantos kWh foi consumido no mes: "))

M = (0.43 * kWh) + 10

Total = M * 1.25 
print(round(Total, 2))