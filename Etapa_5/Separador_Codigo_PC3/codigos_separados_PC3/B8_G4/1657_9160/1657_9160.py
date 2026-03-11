from numpy import *

qp = input("Siglas: ").upper().split(",")
cont = zeros(5, dtype = int)

for i in range(size(qp)):
	if qp[i] == "AZ":
		cont[0] = cont[0] +1
	elif qp[i] == "CA":
		cont[1] = cont[1] +1
	elif qp[i] == "FL":
		cont[2] = cont[2] +1
	elif qp[i] == "PA":
		cont[3] = cont[3] +1
	elif qp[i] == "WI":
		cont[4] = cont[4] +1
print(max(cont))
print(cont)
		
	