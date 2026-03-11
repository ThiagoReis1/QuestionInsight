qntd = int(input(" "))

contadora = 0

while qntd != -1:
	if qntd > 35 and qntd < 95:
		contadora = contadora + 1

	qntd  = int(input(" "))
print(contadora)