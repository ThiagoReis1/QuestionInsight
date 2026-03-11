consumo = float(input("volume:"))

taxa_consumo = 0.37 * consumo

taxa_fixa = 15.00

total = taxa_consumo + taxa_fixa

icms = (total * (35/100))

valor = total + icms

print(round(valor,2))
 