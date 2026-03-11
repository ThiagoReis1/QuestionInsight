from numpy import*
x=input("hwergwiog").split(',')
cont=zeros(6,dtype=int)

for i in x:
	if i.upper()=="MC":
		cont[0]+=1
	elif i.upper()=="C":
		cont[1]+=1
	elif i.upper()=="CM":
		cont[2]+=1
	elif i.upper()=="EM":
		cont[3]+=1
	elif i.upper()=="E":
		cont[4]+=1
	elif i.upper()=="ME":
		cont[5]+=1
print(max(cont))
print(cont)
