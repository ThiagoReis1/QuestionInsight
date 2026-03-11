from numpy import*
z= input("dale: ").split(',')

cont= zeros(5, dtype=int)
for i in z:
	if(i.upper()== "AR"):
		cont[0]= cont[0]+1
	elif(i.upper()== "BR"):
		cont[1]= cont[1]+1
	elif(i.upper()== "CL"):
		cont[2]= cont[2]+1
	elif(i.upper()== "CO"):
		cont[3]= cont[3]+1
	elif(i.upper()== "UY"):
		cont[4]= cont[4]+1
print(max(cont))		
print(cont)