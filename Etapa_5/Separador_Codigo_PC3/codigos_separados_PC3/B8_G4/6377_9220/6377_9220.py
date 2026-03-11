from numpy import *

strg = input("Digite um caractere: ").upper().split(",")
cont = zeros(4, dtype = int)


for i in strg:
	if i == "A":
		cont[0] += 1
	elif i == "B":
		cont[1] += 1
	elif i == "C":
		cont[2] += 1
	elif i == "D":
		cont[3] +=1
		
print (cont)
	
