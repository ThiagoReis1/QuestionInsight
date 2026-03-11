from numpy import*

vet = (input(":")).split(',')

vcont = zeros(5, dtype=int)

for x in vet:
	if (x == "BE"):
		vcont[0] = vcont[0] + 1
	elif (x == "ES"):
		vcont[1] = vcont[1] + 1
	elif (x == "FR"):
		vcont[2] = vcont[2] + 1
	elif (x == "IT"):
		vcont[3] = vcont[3] + 1
	else:
		vcont[4] = vcont[4] + 1

print(max(vcont))
print(vcont)