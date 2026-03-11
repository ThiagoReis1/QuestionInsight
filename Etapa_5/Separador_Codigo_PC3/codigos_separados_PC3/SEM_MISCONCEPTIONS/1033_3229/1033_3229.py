peso = float(input(" digite o valor do peso: "))

custo = (43.21 * peso) + 25.00

icms = (62 / 100) * custo

total = custo + icms

print(round(total,2))