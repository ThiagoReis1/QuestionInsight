from math import*
from numpy import*
a=input("nfgi").split(',')
res=array([0,0,0,0,0])

for i in range (size(a)):
	if(a[i]=="CHN"):
		res[0]=res[0]+1
	elif(a[i]=="JPN"):
		res[1]=res[1]+1
	elif(a[i]=="KOR"):
		res[2]=res[2]+1
	elif(a[i]=="MGL"):
		res[3]=res[3]+1
	
	elif(a[i]=="THA"):
		res[4]=res[4]+1

print(max(res))
print(res)
		
		

