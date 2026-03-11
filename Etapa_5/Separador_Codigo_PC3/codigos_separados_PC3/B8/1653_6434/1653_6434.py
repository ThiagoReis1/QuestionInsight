from numpy import*
string= str(input(": ")).split(',')
cont = zeros(5, dtype=int)

for i in range(len(string)):
	if(string[i]== "AR"):
		cont[0]+=1
	elif(string[i]== "BR"):
		cont[1]+=1
	elif(string[i]=="CL"):
		cont[2]+=1
	elif(string[i]=="CO"):
		cont[3]+=1
	elif(string[i]== "UY"):
		cont[4]+=1
				
maior= 0
for i in cont:
	if(i > maior):
		maior = i
print(maior)
print(cont)
