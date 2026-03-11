from numpy import*
x= input().upper().split(',')
cont = zeros(4,dtype=int)
for i in range(size(x)):
	if x[i] == "E":
		cont[0] +=1
	elif x[i] == "V":
		cont[1] +=1
	elif x[i] == "A":
		cont[2] += 1
	elif x[i] == "D":
		cont[3] +=1
print(cont)