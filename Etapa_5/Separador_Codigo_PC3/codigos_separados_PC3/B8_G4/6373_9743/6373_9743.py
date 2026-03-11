from numpy import*

l = (input("letra:")).upper().split(",")
n = zeros(4,dtype=int)

for i in range(size(l)):
	if l[i]== "A":
		n[0]= n[0]+1
	
	elif l[i]== "P":
		n[1]= n[1]+ 1
	
	elif l[i]== "D":
		n[2]= n[2]+1
	elif l[i]== "M":
		n[3]=n[3]+1
print(n)