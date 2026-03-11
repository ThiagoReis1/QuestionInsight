from numpy import *
pais = input("paises").split(',')
n = zeros(5, dtype = int)
for i in range(size(pais)):
	x = pais[i]
	if(x == "BE" ):
		n[0] = n[0] + 1
	elif(x == "ES" ):
		n[1] = n[1] + 1
	elif(x == "FR" ):
		n[2] = n[2] + 1
	elif(x == "IT" ):
		n[3] = n[3] + 1
	elif(x == "PT" ):
		n[4] = n[4] + 1
m = max(n)
print(m)
print(n)