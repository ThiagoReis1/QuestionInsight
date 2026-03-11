from math import * 
a = float(input("Consumo de kWh: "))

b = 0.43 * a
c = b + 10
d = c * 0.25
e = c + d
print(round(e,2))