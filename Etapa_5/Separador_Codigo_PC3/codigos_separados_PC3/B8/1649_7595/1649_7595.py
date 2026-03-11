from numpy import *

strg = input("Cor: ").split(',')

cores_contagem = zeros(5, dtype = int)

for i in range (len(strg)):
	if(strg[i].upper() == "P"):
		cores_contagem[0] += 1
	elif(strg[i].upper() == "C"):
		cores_contagem[1] += 1
	elif(strg[i].upper() == "M"):
		cores_contagem[2] += 1
	elif(strg[i].upper() == "V"):
		cores_contagem[3] += 1
	elif(strg[i].upper() == "A"):
		cores_contagem[4] += 1
	
print(max(cores_contagem))
print(cores_contagem)