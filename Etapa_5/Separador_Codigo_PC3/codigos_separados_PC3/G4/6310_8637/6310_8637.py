from numpy import *
g=input().upper()
cont=0
i=0
while i<len(g):
	if g[i]=="M":
		cont+=7.25
	if g[i]== "P":
		cont+=4.75
	if g[i]== "R":
		cont+=3.50
	i+=1
	cont
print(round(cont,2))