from numpy import *

a = input("insira: ").upper().split(",")

b = zeros(4, dtype=int)

for i in range(len(a)):
	if(a[i] == "E"):
		b[0] +=1
	elif(a[i] == 'V'):
		b[1] += 1
	elif(a[i] == 'A'):
		b[2] += 1
	elif(a[i] == 'D'):
		b[3] +=1
		
print(b)		
		
	
		
	
