kwh = float(input("kWh: "))

v1 = (kwh * 0.43 + 10)
v2 = (v1 * (25/100))
total = v1 + v2
print(round(total,2))
