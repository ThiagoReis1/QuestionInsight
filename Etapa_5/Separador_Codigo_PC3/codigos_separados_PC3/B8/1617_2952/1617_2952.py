from numpy import*
esp=array(eval(input("Tipo de espada: ")))
niv=array(eval(input("Nível: ")))

i=0
dano1=0
dano2=0
dano3=0
dano4=0
dano5=0

while (i<size(niv)):
	if (esp[i]=="CENOURA"):
		dano1=2*niv[i]+dano1
	elif (esp[i]=="FERRO"):
		dano2=4*niv[i]+dano2
	elif (esp[i]=="DWARVEN"):
		dano3=8*niv[i]+dano3
	elif (esp[i]=="ELVEN"):
		dano4=11*niv[i]+dano4
	elif (esp[i]=="DAEDRIC"):
		dano5=14*niv[i]+dano5
	i=i+1
dano_total=dano1+dano2+dano3+dano4+dano5

print(dano_total)