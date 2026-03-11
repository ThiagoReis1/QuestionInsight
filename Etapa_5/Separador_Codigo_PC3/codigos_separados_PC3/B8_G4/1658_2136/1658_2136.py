from numpy import*
p = input("digite os paises: ").split(',')
cont= zeros(5,dtype = int)

i=0
c=0
j=0
k=0
m=0
t=0
while(i<size(p)):
	if(p[i]== "CHN"):
		c = c +1
	elif(p[i]== "JPN"):
		j = j +1
	elif(p[i]== "KOR"):
		k = k + 1
	elif(p[i]== "MGL"):
		m = m + 1
	elif(p[i]== "THA"):
		t=t+1
	i=i+1
cont[0]=c
cont[1]=j
cont[2]=k
cont[3]=m
cont[4]=t
print(max(cont))
print(cont)