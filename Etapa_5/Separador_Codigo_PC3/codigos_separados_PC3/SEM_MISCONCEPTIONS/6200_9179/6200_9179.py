altura_max = 1.75
taxa_max = 0.01
anos = 0

altura_c = float(input("Altura do Max: "))
taxa_c = float(input("Taxa de crescimento: "))

while altura_c < altura_max:
	altura_max += taxa_max
	altura_c += taxa_c
	anos += 1
print(anos)
