roleta = input(": ").upper()

s = 0

p = 0

cem = 100

while (roleta != "S"):
	s = s + 1
	if (roleta == "PRETA"):
		p = p + 1
	roleta = input(": ").upper()
porc = p / s
final = porc * 100
print(s)
print(round(final, 2))
