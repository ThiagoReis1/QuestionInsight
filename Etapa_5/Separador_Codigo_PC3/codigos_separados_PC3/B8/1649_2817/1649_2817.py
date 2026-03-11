from numpy import *

vet = input("").split(",")

qntd_cores = zeros(5, dtype=int)

for i in vet:
	if(i.upper() == "P"):
		qntd_cores[0] += 1
	elif(i.upper() == "C"):
		qntd_cores[1] += 1
	elif(i.upper() == "M"):
		qntd_cores[2] += 1
	elif(i.upper() == "V"):
		qntd_cores[3] += 1
	elif(i.upper() == "A"):
		qntd_cores[4] += 1
		
print(max(qntd_cores))
print(qntd_cores)