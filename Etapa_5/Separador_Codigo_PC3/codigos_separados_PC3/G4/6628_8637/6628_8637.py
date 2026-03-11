from numpy import *

s=input().upper()
i=0
cont=0
while i<len(s):
	if s[i]== "E":
		cont+=1
	i+=1
print(cont)
	
