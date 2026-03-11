from numpy import*
vcus = array(eval(input("vetor custo: "))) 
j = 0
i = 0
cont = 0
while (cont < size(vcus)):
	if(vcus[i] > 80.0):
		custo1 = vcus[i] - 5.00
		i = i + 1 
	else:
		custo2 = vcus[j]
		j = j + 1
	cont = cont + 1 
custot = custo1 + custo2
print(custot)
