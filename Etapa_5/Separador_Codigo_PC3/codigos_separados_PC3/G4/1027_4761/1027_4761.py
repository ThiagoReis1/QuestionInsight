a = float(input('kWh consumidos: '))
b = float(0.43*a+10)
c = float(b+(b*25/100))
print(round(c, 2))