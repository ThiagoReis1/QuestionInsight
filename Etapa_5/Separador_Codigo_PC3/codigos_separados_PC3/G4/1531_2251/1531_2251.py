from math import*
x = eval(input("x: "))
k = int(input("k: "))
i = 1
a = 2
s = x
sinal = -1
while(i<k):
	s = s + sinal * (x ** a/factorial(a))
	a = a + 2
	sinal = 1 
	i = i + 1
print(round(s,10))
	
	
	

