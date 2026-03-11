from numpy import *

nomes = array(eval(input("Nomes dos times: ")))

conta = zeros(4, dtype = int)

for i in nomes:
	if (i.upper() == "BOTAFOGO"):
		conta[0] += 1
	elif (i.upper() == "FLAMENGO"):
		conta[1] += 1
	elif (i.upper() == "FLUMINENSE"):
		conta[2] += 1
	elif (i.upper() == "VASCO"):
		conta[3] += 1
		
print(conta)