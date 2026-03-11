consumo = float(input())

total_consumo = (0.28 * consumo) + 23.0

total_imposto = total_consumo * (31/100)

total_pagar = total_consumo + total_imposto

print(round(total_pagar, 2))