from numpy import*
cor = input()
cor = cor.split(',')
cont = zeros(5, dtype=int)
x=0
while x < size(cor):
	if cor[x] == "P":
		cont[0]= cont[0]+1
	elif cor[x] == "C":
		cont[1]= cont[1]+1
	elif cor[x] == "M":
		cont[2]= cont[2]+1
	elif cor[x] == "V":
		cont[3]= cont[3]+1
	elif cor[x] == "A":
		cont[4]= cont[4]+1	
	x=x+1	
print(max(cont))
print(cont)