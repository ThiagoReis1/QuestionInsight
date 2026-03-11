from math import*
from numpy import*
str=input()
x=str.split(',')
aux=zeros(5,dtype=int)

for i in range(size(x)):
	if x[i]=="CHN":
		aux[0]=aux[0]+1
	elif x[i]=="JPN":
		aux[1]=aux[1]+1
	elif x[i]=="KOR":
		aux[2]=aux[2]+1
	elif x[i]=="MGL":
		aux[3]=aux[3]+1
	elif x[i]=="THA":
		aux[4]=aux[4]+1
print(max(aux))
print(aux)