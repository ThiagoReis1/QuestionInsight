from numpy import *
fras = input("insert countries: ").split(',')
paises = zeros(5,dtype=int)
for i in range(size(fras)):
	if(fras[i].upper() == "BE"):
		paises[0] = paises[0] + 1
	elif(fras[i].upper() == "ES"):
		paises[1] = paises[1] + 1
	elif(fras[i].upper() == "FR"):
		paises[2] = paises[2] + 1
	elif(fras[i].upper() == "IT"):
		paises[3] = paises[3] + 1
	elif(fras[i].upper() == "PT"):
		paises[4] = paises[4] + 1
record = 0
for g in range(size(paises)):
	if(paises[g] >= record):
		record = paises[g]
print(record)
print(paises)