result = input(" digite o nome do curso: ")
x = 0
n = 0
while(result.upper() != "S"):
	if (result.upper() == "ICOMP"):
		x=x+1
	result = input(" digite o nome do curso: ")
print(x)