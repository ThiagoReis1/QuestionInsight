from numpy import*
x = input ("Digite vetor: ").upper().split(",")
vcont = zeros(5, dtype=int)
for i in range (size (x)) :
	if (x[i] == "AM") :
		vcont[0] = vcont[0] + 1
	elif (x[i]== "PE") :
		vcont[1] = vcont[1] + 1
	elif (x[i]== "MG") :
		vcont[2] = vcont[2] + 1
	elif (x[i]== "SP") :
		vcont[3] = vcont[3] + 1
	elif (x[i]== "RS") :
		vcont[4] = vcont[4] + 1
print(max(vcont))
print (vcont)