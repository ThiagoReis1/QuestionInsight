from numpy import*
vbanho = array(eval(input("Digite o vetor tempo no banho(em minutos): ")))
modo = array(eval(input("Digite o vetor modo de banho (QUENTE, MORNO OU FRIO): ")))

i=0
total = 0

while(i<size(vbanho)):
	if(modo[i]=="QUENTE"):
		total = total + vbanho[i]*90*0.005
	elif(modo[i]=="MORNO"):
		total = total + vbanho[i]*45*0.005
	elif(modo[i]=="FRIO"):
		total = total + vbanho[i]*0*0.005
	i=i+1

print(round(total,2))

