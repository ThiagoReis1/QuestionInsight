valor = float(input("qual foi o valor da encomenda? "))

imposto = valor * (81/100)

total = valor + imposto + 12.00

print(round(total, 2))