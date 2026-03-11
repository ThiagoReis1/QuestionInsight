from math import * 
x = float (input("numero "))
k = int(input("quantidade de termos"))
result = 0 
cont = 0
r = 1
while (cont != k):
	result += pow (x,r)/r
	r += 2
	cont += 1 
 	
print(round(result,7))