from numpy import*
v=input("").upper().split(",")
z=zeros(4, dtype=int)

for i in range(size(v)):
	if v[i]=="O":
		z[0]+=1
	elif v[i]=="D":
		z[1]+=1
	elif v[i]=="N":
		z[2]+=1
	elif v[i]=="C":
		z[3]+=1
print(z)