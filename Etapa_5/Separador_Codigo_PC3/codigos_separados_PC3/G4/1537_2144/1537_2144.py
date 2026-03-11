from math import*

x = float(input("número:"))
k = int(input("quantidade de termos da série:"))

i = 0
s = 0

while(i < k):
	e = ((x ** i) / factorial(i))
	s = s + e
	i = i + 1
	
print(round(s,9))