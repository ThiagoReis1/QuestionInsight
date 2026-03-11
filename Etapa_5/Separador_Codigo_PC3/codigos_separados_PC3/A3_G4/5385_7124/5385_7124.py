from numpy import*

v= input().upper()
i=0
c=0
t=0

while c<len(v):
	if v[c]== "A" or v[c]== "E" or v[c]== "I" or v[c]=="O" or v[c]=="U":
		t= t+35.15
	else:
		t= t+42.17
	c= c+1
	
print (round(t,2))

