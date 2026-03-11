from math import*
x = float(input("x: "))
k = int (input("k: "))
a = 0
c = 0
while(c < k):
	a = a + ((-1)**c)*((x**(2*c+1))/(2*c+1))
	c = c + 1
print(round(a,6))