from numpy import*
vet= input("cor").split(',')
v=zeros(5,dtype(int))

for j in range (size(vet)):
	if (vet[j] == "P"):
		v[0]= v[0]+1
	elif (vet[j]== "C"):
		v[1]= v[1]+1
	elif (vet[j]== "R"):
		v[2]= v[2]+1
	elif (vet[j]== "L"):
		v[3]= v[3]+1
	elif (vet[j]== "B"):
		v[4] = v[4]+1
print(max(v))
print(v)
