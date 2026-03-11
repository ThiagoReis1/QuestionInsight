mol = input("Digite Glicina ou Serina: ").upper()

glicina = (2 * 12.011) + (5 * 1.0079) + (1 * 14.00674) + (2 * 15.9994)
serina = (3 * 12.011) + (7 * 1.0079) + (1 * 14.00674) + (3 * 15.9994)




if (mol == "SERINA"):
	print(round(serina, 2))
else:
	print(round(glicina, 2))