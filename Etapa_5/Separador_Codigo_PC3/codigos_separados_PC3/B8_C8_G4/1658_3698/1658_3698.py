from numpy import * 

p = input("Digite: ").split(",")
cont=zeros(5, dtype=int)
i=0
c=0
j=0
k=0
m=0
t=0

for i in range(size(p)):
	if p[i]=="CHN":
		c+=1
		cont[0]+=1
	elif p[i]=="JPN":
		j+=1
		cont[1]+=1
	elif p[i]=="KOR":
		k+=1
		cont[2]+=1
	elif p[i]=="MGL":
		m+=1
		cont[3]+=1
	elif p[i]=="THA":
		t+=1
		cont[4]+=1
	i+=1
m1=max(c,j,k,m,t)
print(m1)
print(cont)
	
		
		
		