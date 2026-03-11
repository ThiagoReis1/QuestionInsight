from numpy import*
c= input('inserir caractere:').upper().split(",")
v= zeros(4,dtype=int)

for i in range(size(c)):
	if c[i]=="C":
		v[0]+=1
	elif c[i]=="O":
		v[1]+=1
	elif c[i]=="P":
		v[2]+=1
	elif c[i]=="E":
		v[3]+=1
print(v)
		