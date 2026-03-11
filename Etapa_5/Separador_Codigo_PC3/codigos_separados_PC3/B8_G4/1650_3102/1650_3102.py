from numpy import*
v=input("cores:").split(",")
vz =zeros(5, dtype = int)
p=0
c=0
r=0
l=0
b=0

for x in v:
	if(x=="P"):
		p = p + 1
	elif(x=="C"):
		c = c + 1
	elif(x=="R"):
		r = r + 1
	elif(x=="L"):
		l = l + 1
	elif(x=="B"):
		b = b + 1
vz[0]=p
vz[1]=c
vz[2]=r
vz[3]=l
vz[4]=b

print(max(vz))
print(vz)