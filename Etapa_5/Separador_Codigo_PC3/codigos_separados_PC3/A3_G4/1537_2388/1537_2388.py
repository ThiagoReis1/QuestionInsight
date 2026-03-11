from math import*

x = float(input("num :"))
k = int(input("quantidade de termos: "))


y = 1
t= 0
e = 0
m=1

while(t < k):
	m= 1 + e
	e = e+  ((x ** y)/ factorial(y))
	y = y + 1
	t = t + 1
print(round(m,9))

