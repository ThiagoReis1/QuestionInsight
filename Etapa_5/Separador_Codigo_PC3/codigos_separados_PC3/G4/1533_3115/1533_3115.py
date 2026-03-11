from math import*
x = float(input(""))
k = int(input(""))
s = 0
c = 0
a = 0
while(c<k):
		
		s = s + x**(a)/factorial(a)
		a = a + 2
		c = c + 1
print(round(s,8))