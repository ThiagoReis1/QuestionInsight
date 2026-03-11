from numpy import*

s=input('')
v=s.split(',')
AC=0
AM=0
PA=0
RO=0
RR=0
cop=zeros(5, dtype=int)
for i in range(size(v)):
	if v[i]=="AC":
		cop[0]=cop[0]+1
	if v[i]=="AM":
		cop[1]=cop[1]+1
	if v[i]=="PA":
		cop[2]=cop[2]+1
	if v[i]=="RO":
		cop[3]=cop[3]+1
	if v[i]=="RR":
		cop[4]=cop[4]+1


m= max(cop)		
print(m)
print(cop)