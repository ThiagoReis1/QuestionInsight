cons = float(input("kWh consumidos no mes: "))
valor = (0.43 * cons) + 10
icms = (25/100) * valor
print(round(valor + icms, 2))