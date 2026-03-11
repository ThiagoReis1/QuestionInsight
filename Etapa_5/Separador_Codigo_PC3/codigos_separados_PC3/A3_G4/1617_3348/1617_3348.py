from numpy import*

d = [2,4,8,11,14]
v = array(eval(input("Tipo de espada: ")))
u = array(eval(input("Level: ")))
i= 0
dano = 0
while(i<size(u)):
	if(v[i]=="CENOURA"):
		dda = (2)
	if(v[i]=="FERRO"):
		dda = (4)
	if(v[i]=="DWARVEN"):
		dda = (8)
	if(v[i]=="ELVEN"):
		dda = (11)
	if(v[i]=="DAEDRIC"):
		dda = 14
	dano = dano + dda*u[i]
	i = i + 1
print(int(dano))
