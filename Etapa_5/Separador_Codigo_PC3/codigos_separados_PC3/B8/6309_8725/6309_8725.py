from numpy import*
r= input("dgt:")

i=0
cont=0
cont1= 0
cont2= 0
cont3= 0

while i < len(r):
	if r[i] == "H":
		cont=cont+5.40
		cont1=cont1+1
	elif r[i] == "C":
		cont=cont+8.95
		cont2=cont2+1
	elif r[i] == "L":
		cont=cont+4.50
		cont3=cont3+1
	i=i+1
	
T = round(cont,2)
print(T, cont1, cont2, cont3)
		
	


