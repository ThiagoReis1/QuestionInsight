minutos = float(input("Insira a minutagem consumida no mes: "))

y = 0.28 * minutos + 23

imposto = y * (31/100)

total = imposto + y

print(round(total,2))