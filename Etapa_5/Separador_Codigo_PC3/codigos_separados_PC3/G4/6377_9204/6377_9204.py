from numpy import*

J = input("digite os jogadores:").upper() .split(",")
cont = zeros(4 ,dtype=int)

for i in range(size(J)):
	if J[i] =="A":
		cont[0] = cont[0] + 1
		
	elif J[i] =="B":
		cont[1] = cont[1] + 1
	
	elif J[i] =="C":
		cont[2] = cont[2] + 1
	
	else:
		cont[3] = cont[3] + 1
print(cont)