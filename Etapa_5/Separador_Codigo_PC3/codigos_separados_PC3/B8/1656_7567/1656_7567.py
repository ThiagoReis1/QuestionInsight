from numpy import*
paises = input("").upper().split(',')
quant = zeros(5,dtype = int)
for i in range(size(paises)):
	if(paises[i] == "BE"):
		quant[0] = quant[0] + 1
	elif(paises[i] == "ES"):
		quant[1] = quant[1] + 1
	elif(paises[i] == "FR"):
		quant[2] = quant[2] + 1
	elif(paises[i] == "IT"):
		quant[3] = quant[3] + 1
	elif(paises[i] == "PT"):
		quant[4] = quant[4] + 1
if(quant[0] > quant[1] and quant[0] > quant[2] and quant[0] > quant[3] and quant[0] > quant[4]):
	print(quant[0])
elif(quant[1] > quant[2] and quant[1] > quant[3] and quant[1] > quant[4]):
	print(quant[1])
elif(quant[2] > quant[3] and quant[2] > quant[4]):
	print(quant[2])
elif(quant[3] > quant[4]):
	print(quant[3])
else:
	print(quant[4])
print(quant)