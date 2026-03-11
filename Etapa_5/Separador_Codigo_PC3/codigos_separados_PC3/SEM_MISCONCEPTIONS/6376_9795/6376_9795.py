from numpy import*
gol = input("sequencia de gols: ").upper().split(',')
cont0=0
cont1=0
cont2=0
cont3=0

for i in gol:
	if  i== "A":
		cont0 +=1
	if i == "B":
		cont1 +=1
	if i== "C":
		cont2 +=1
	if i == "D":
		cont3 +=1
		
cont=array([cont0,cont1,cont2,cont3])
print(cont)