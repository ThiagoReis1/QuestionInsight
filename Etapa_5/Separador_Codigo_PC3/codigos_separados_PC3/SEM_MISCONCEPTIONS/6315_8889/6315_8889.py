from numpy import*
pr=input("").upper()
v = 0
i=0
cont_1= 0
cont_2= 0
cont_3= 0
while i< len(pr):
	if pr[i]=="I":
		v += 3.75
		cont_1 +=1
	if pr[i]=="M":
		v+= 4.50
		cont_2 +=1
	if pr[i]=="S":
		v+= 2.90
		cont_3 +=1
	i= i+1
print(round(v,2),cont_1,cont_2,cont_3)
