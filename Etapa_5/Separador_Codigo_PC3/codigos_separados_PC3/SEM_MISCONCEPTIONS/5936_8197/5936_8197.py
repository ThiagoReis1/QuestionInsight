consumo = float(input("Qual foi o consumo mensal em kWh? "))

valor = (consumo * 0.43) + 10.00

ICMS = valor / 4

valor_total = valor + ICMS

print(round(valor_total,2))