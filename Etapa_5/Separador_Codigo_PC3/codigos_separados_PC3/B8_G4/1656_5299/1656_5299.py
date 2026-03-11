from numpy import *
st = input("").upper().split(',')
cont = zeros(5,dtype=int)

for i in range(size(st)):
	if (st[i] == "BE"):
		cont[0] = cont[0]+1
	elif(st[i] == "ES"):
		cont[1] = cont[1]+1
	elif (st[i] == "FR"):
		cont[2] = cont[2]+1
	elif (st[i]== "IT"):
		cont[3] = cont[3]+1
	elif (st[i] == "PT"):
		cont[4] = cont[4]+1
print(max(cont))
print(cont)