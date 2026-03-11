from math import*
x = float(input(": "))
k = int(input(": "))
e = 0
t = 0
while(t < k):
	e =  e + (x**t)/(factorial(t))  
	t = t + 1
print(round(e, 9))