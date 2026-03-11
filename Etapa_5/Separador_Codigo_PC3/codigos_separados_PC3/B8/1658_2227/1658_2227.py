from numpy import*
vet=input("paises: ").split(",")

formula= zeros(5, dtype=int)

for i in vet:
	if (i.upper()== "CHN"):
		formula[0] += 1
	elif (i.upper() == "JPN"):
		formula[1] +=1
	elif (i.upper()=="KOR"):
		formula[2] +=1
	elif (i.upper()=="MGL"):
		formula[3] +=1
	elif (i.upper()== "THA"):
		formula[4] +=1
		
print(max(formula))
print(formula)