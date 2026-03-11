from numpy import *

pais = input("pais: ").upper().split(",")
resultado = zeros(5,dtype = int)
cont = 0
for i in range(size(pais)):
	if(pais[i] == "BE"):
		resultado[0] = resultado[0] + 1
	elif(pais[i] == "ES"):
		resultado[1] = resultado[1] + 1
	elif(pais[i] == "FR"):
		resultado[2] = resultado[2] + 1
	elif(pais[i] == "IT"):
		resultado[3] = resultado[3] + 1
	elif(pais[i] == "PT"):
		resultado[4] = resultado[4] + 1
print(max(resultado))
print(resultado)