valor = float(input("Valor da encomenda: "))

imposto = valor * (81 / 100)

taxa = 12.0

total = valor + imposto + taxa

print(round(total, 2))