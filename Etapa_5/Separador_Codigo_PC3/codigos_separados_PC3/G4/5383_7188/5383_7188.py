from numpy import*
e= input()
i=0
t=0
v= 0.12
nv= 0.18
while i < len(e):
	if e[i]== "A"or e[i]=="E"or e[i]=="I"or e[i]=="O"or e[i]=="U": 
		t= t + v 
	else:
		t= t + nv 
	i= i+1
print(round(t,2))