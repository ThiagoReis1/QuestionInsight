p = float(input("quanto foi consumido no mes: "))
kwh = float(0.43)
taxa = int(10)
imposto = (25/100)
parcial = (p*kwh+taxa)*(imposto)
final = (p*kwh+taxa)+parcial
print(round(final,2))