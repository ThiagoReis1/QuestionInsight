from numpy import*

n=input("nacionalidade").upper().split(',')
p=zeros(5, dtype=int)


for i in range(size(n)):
	if(n[i]== "AR"):
		p[0]= p[0] +1
	elif(n[i]=="BR"):
		p[1]= p[1]+1
	elif(n[i]=="CL"):
		p[2]=p[2]+1
	elif(n[i]=="CO"):
		p[3]=p[3]+1
	elif(n[i]=="UY"):
		p[4]=p[4]+1
print(max(p))
print(p)
		