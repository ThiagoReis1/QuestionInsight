from numpy import*
atk=array(eval(input(":")))
i=0
j=1
dano=0
while(i<size(atk)):	
	dano=dano+(atk[i]*j)
	j=j+1
	i=i+1
print(dano)