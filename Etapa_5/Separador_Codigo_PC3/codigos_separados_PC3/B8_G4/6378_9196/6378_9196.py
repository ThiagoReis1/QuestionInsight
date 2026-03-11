from numpy import*
n= input("notas:").upper().split(",")
n1= zeros(4, dtype=int)
for i in range(size(n)):
	if n[i]== "C":
		n1[0]+=1
	elif n[i]=="D":
		n1[1]+=1
	elif n[i]=="V":
		n1[2]+=1
	elif n[i]=="U":
		n1[3]+=1
print(n1)