from numpy import *
at1= array(eval(input("atv fisicas: ")))
at2= array(eval(input("gasto calorico: ")))
calorias= [3.0,10.3,6.7,9.7,5.0]
i=0
j=0
soma=0
while(i<size(at1)):
	if(at1[i]=="ALONGAMENTO"):
			soma=soma+at2[0]*calorias[i]
		j=j+1
	elif(at1[i]=="CORRIDA"):
			soma=soma+at2[1]*calorias[i]
	elif(at1[i]=="DANCA"):
			soma=soma+at2[2]*calorias[i]
	elif(at1[i]=="DANCA"):
			soma=soma+at2[2]*calorias[i]
	elif(at1[i]=="DANCA"):
			soma=soma+at2[2]*calorias[i]		
		
print(round(soma,2))	