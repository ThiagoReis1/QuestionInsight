agua = float(input("conta de agua"))
tratamento = (0.37 * agua) + 15
ICMS = (35/100) * tratamento
total = ICMS + tratamento
print(round(total, 2))