from numpy import*

vet = array(eval(input("")))

vcont = zeros(4, dtype=int)
#vcont = 0
for x in vet:
	if (x == "BOTAFOGO"):
		vcont[0] = vcont[0] + 1
	elif (x == "FLAMENGO"):
		vcont[1] = vcont[1] + 1
	elif (x == "FLUMINENSE"):
		vcont[2] = vcont[2] + 1
	else:
		vcont[3] = vcont[3] + 1
	
print(vcont)