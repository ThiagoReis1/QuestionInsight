from numpy import *
string = input("a: ").upper().split(",")
cont = zeros(5, dtype=int)
if string == "AZ":
	cont[0] = 	
elif string == "CA":
	cont[1] += 1
elif string == "FL":
	cont[2] += 1	
elif string == "PA":
	cont[3] += 1	
else: 
	cont[4] += 1
print(cont)
maximo = max(cont)
print(maximo)