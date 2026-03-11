from numpy import*
x= zeros (4,dtype=int)
c= input("num:").upper().split(",")
 
for i in range (size(c)):
	if c[i]== "A":
		x[0]= x[0]+1
	elif c[i]=="B":
		x[1]=x[1]+1
	elif c[i]=="L":
		x[2]=x[2]+1
	elif c[i]=="H":
		x[3]=x[3]+1
print(x)
		
		