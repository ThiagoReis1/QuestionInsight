from math import *

x = float(eval(input("")))
k = int(input(""))



n = 0
cos = 0
cont = 0
j =-1

while cont < k:
	
	cos = cos + ((x**n)/factorial(cont))*((j)**(cont))
	n = n + 1
	cont = cont + 2
					 
print(round(cos,6))