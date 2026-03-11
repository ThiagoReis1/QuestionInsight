from numpy import*
v= input("vetor").split(',')
copia= zeros(5, dtype=int)
for x in v:
	if x== "AC":
		copia[0]=copia[0]+1
	elif x== "AM":
		copia[1]=copia[1]+1	
	elif x== "PA":
		copia[2]=copia[2]+1	
	elif x== "RO":
		copia[3]=copia[3]+1	
	elif x== "RR":
		copia[4]=copia[4]+1	
print(max(copia))
print(copia)