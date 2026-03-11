t = input("qual a escala? (C) para celsius ou (K) para kelvin: ").upper()
c = float(input(" qual a temperatura: "))

total = 0

if t == "C":
	total = c + 273.15
else:
	total = c - 273.15
	
print(round(total, 2))

