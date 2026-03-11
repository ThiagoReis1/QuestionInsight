from numpy import *
x = float(input(""))
k = int(input(""))

s = 0
d = 1
for i in range (1, k+ 1, 2):
	s = s+(x**i)/i
	d = d +2
	
print(round(s,7))