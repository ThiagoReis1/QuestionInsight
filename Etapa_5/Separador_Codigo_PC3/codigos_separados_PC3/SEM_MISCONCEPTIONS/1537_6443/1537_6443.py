from math import * 
x = eval(input( ))
k = int(input( ))
soma= 0
soma+=x

for i in range (1,k):
     if i%1 == 0:
	      soma+= (x**(i*1+1))/factorial(i*1+1)
	else: 
		   soma-= (x**(i*1+1))/ factorial(i*1+1)
print(round(soma,9))
