from math import*
x = oval(input(": "))
k = int(input(": "))

i = 1
e = 0


while (i<k):	
	e = e + (x**(1+i))/factorial(1*i+1)		
	i = i + 1
print(round(e,8))	