from numpy import *

rotulo = input("Diigite o rotulo: ").upper()

i = 0
qv = 0 #quantidade vogal
qnv = 0 #quantidade noa vogal

while(i < len(rotulo)):
	if(rotulo[i] == "A") or (rotulo[i] == "E") or (rotulo[i] == "I") or (rotulo[i] == "O") or (rotulo[i] == "U"):
		qv = qv + 1
	else:
		qnv = qnv + 1
	
	i = i + 1
	
	vogal = (qv * 0.19)
	nvogal = (qnv * 0.23)
	custo = vogal + nvogal
	
print(round(custo, 2))