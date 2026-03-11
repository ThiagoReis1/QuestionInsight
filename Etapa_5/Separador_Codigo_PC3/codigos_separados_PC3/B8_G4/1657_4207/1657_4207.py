from numpy import *

es= input("Estados: ").split(',')

x= zeros(5,dtype=int)

for i in range(size(es)):
	if(es[i]=='AZ'):
		x[0]=x[0]+1
	elif(es[i]=='CA'):
		x[1]=x[1]+1
	elif(es[i]=='FL'):
		x[2]=x[2]+1
	elif(es[i]=='PA'):
		x[3]=x[3]+1
	elif(es[i]=='WI'):
		x[4]=x[4]+1
		
print(max(x))
print(x)
