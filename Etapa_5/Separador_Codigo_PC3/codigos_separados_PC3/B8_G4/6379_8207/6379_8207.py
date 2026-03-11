from numpy import*

c=input("").upper().split(",")
z= zeros(5, dtype=int)

for i in range(size(c)):
	if c[i]=="A":
		z[0]+=1
	elif c[i]=="B":
		z[1]+=1
	elif c[i]=="C":
		z[2]+=1
	elif c[i]=="D":
		z[3]+=1
	elif c[i]=="E":
		z[4]+=1
print(z)