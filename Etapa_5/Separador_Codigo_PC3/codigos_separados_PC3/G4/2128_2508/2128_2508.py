from numpy import *
vet = array(eval(input(":")))

vet1 = vet 
MF = (sum(vet1) - max(vet)) /3.0
print(round(MF, 2))
if(MF >= 50.0):
	print("APROVADO")
else:
	print("REPROVADO")