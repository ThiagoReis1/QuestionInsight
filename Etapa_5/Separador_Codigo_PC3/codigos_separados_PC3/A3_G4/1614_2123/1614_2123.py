from numpy import*
veta = array(eval(input("digite o alimento:").upper()))
vtq = array(eval(input("calorias: ")))
i = 0
v = 0
v1 = 0
v2 = 0
v3 = 0
v4 = 0
while(i<size(veta)):
	if(veta[i] == "BANANA"):
		v = vtq[i]*0.97
	if(veta[i] == "BIFE"):
		v1 = vtq[i]*2.95
	if(veta[i] == "FEIJOADA"):
		v2 = vtq[i]*1.27
	if(veta[i] == "OMELETE"):
		v3 = vtq[i]*1.04
	if(veta[i]== "TOMATE"):
		v4 = vtq[i]*0.2
	i = i+1
print(round(v+v1+v2+v3+v4,2))	