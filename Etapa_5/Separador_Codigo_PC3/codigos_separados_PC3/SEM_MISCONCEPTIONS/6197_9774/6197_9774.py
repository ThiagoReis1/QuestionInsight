altali = 1.6
taxali = 0.02

anos = 0

alt = float(input("Altura: "))
tax = float (input("Taxa de crescimento: "))

while (alt < altali):
	alt += tax
	altali += taxali
	anos += 1

print(anos)