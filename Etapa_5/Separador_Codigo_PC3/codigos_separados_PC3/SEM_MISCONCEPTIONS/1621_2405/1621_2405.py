from numpy import*
vet1 =array(eval(input("digite o vet1: ")))
vet2= array(eval(input("digite o vet2: ")))

i = 0
t = 0

ARROZ = 1.25
FEIJAO = 2.60
BIS = 1.80
MIOJO = 0.85
FANTA = 3.20

while(i<size(vet1)):
	if(vet1[i] == "ARROZ"):
		t = t + vet2[i]*ARROZ
	elif(vet1[i] == "FEIJAO"):
		t = t + vet2[i]*FEIJAO
	elif(vet1[i] == "BIS"):
		t = t + vet2[i]*BIS
	elif(vet1[i] == "MIOJO"):
		t = t + vet2[i]*MIOJO
	else:
		t = t + vet2[i]*FANTA
	i = i + 1
print(round(t, 2))





