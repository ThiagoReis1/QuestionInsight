from math import*
x = float(input("insira x: "))
k = int(input("insira k: "))

c = 1 
K = 0

while(k>0):
	c = c + (x**(1*k+2))/(factorial(1*k+2))
	K = K + 1
print(round(c, 8))