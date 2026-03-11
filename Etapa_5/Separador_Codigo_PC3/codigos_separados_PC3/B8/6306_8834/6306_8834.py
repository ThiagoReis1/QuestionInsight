from numpy import*
r=input("")
i=0
cont=0
cont_1=0
cont_2=0
cont_3=0
while i <len(r):
	if r[i]=="A":
		cont=cont+19.90
		cont_1=cont_1+1
	elif r[i]=="L":
		cont=cont+3.50
		cont_2=cont_2+1
	elif r[i]=="P":
		cont=cont+4.25
		cont_3=cont_3+1
	i=i+1
	t=round(cont,2)
	
print(round(t,2),cont_1,cont_2,cont_3)
	