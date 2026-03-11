
kWh = 0.43
x = 10
aumento = 25 / 100
y = float(input("kWh consumidos no mes: "))
subtotal = kWh * y + 10
total = (subtotal + subtotal * (25 / 100))
print(round(total, 2))