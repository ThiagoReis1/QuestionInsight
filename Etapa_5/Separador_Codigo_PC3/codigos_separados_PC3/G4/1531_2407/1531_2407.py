from math import*
x = eval(input("Ângulo: "))
k = int(input("N da série: "))

c = 1
cos = 1
f = 2
sinal = -1 

while (c < k):
	
	cos = cos + (x**f/factorial(f)) * sinal
	f = f+2
	c = c+1
	sinal = sinal * -1
	
print(round(cos, 10))