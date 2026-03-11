from numpy import*

espada=array(eval(input("digite nomes: ")))
tipo=array(eval(input("digite tipo: ")))

dano=0
i=0
while(i<size(espada)):
	if(espada[i]=="CENOURA"):
		dano=dano+tipo[i]*2
	elif(espada[i]=="FERRO"):
		dano=dano+tipo[i]*4
	elif(espada[i]=="DWARVEN"):
		dano=dano+tipo[i]*8
	elif(espada[i]=="ELVEN"):
		dano=dano+tipo[i]*11
	elif(espada[i]=="DAEDRIC"):
		dano=dano+tipo[i]*14
	i=i+1
print(dano)