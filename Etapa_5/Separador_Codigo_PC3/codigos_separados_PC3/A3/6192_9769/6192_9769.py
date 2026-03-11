resu = input('').upper()

num = 0
quant = 0

while resu != 'S':
	if resu == "PRETA":
		quant += 1
	num+= 1
	
	resu = input('').upper()
	
print(quant)
