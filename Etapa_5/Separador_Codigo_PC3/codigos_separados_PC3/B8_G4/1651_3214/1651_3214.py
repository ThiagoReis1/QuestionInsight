from numpy import *
v=str(input()).split(",")
x=zeros(6,dtype=int)
MC=0
C=0
CM=0
EM=0
E=0
ME=0
for i in v:
	if i=="MC":
		MC=MC+1	
	elif i=="C":
		C=C+1
	elif i=="CM":
		CM=CM+1
	elif i=="EM":
		EM=EM+1	
	elif i=="E":
		E=E+1
	elif i=="ME":
		ME=ME+1
x[0]=MC
x[1]=C
x[2]=CM
x[3]=EM
x[4]=E
x[5]=ME
print(max(x))
print(x)
		
	