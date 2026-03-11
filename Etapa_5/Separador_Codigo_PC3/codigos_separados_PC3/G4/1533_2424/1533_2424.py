from math import *
x = eval(input("num real: "))
k = int(input("num inteiro: "))
t = 0
a = 0
while(t<k):
	a = a + (x**(2*t))/(factorial(2*t))
	t = t +1
print(round(a,8))


