p = str(input("")).upper
cont = 0

while p != "S":
	if p == ("SIM", "NA", "S"):
		cont = cont + 1
		print(cont)