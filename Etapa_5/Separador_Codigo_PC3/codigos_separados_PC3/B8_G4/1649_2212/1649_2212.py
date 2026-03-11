from numpy import *
k = input("Qual as iniciais? ").upper().split()
s=zeros(5,dtype=int)
p=0
c=0
m=0
v=0
a=0
for i in range(len(k)):
	if(k[i]=="P"):
		p=p+1
		s[0]=p
	elif(k[i]=="C"):
		c=c+1
		s[1]=c
	elif(k[i]=="M"):
		m=m+1
		s[2]=m
	elif(k[i]=="V"):
		v=v+1
		s[3]=v
	elif(k[i]=="A"):
		a=a+1
		s[4]=a
print(max(s))
print(s)
