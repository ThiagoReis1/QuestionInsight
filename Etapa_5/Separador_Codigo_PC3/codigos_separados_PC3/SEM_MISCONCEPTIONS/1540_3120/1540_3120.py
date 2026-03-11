from math import*
x = eval(input(""))
k = int(input(""))

result = 0;
sinal = 1
cont = 0;
r = 1;
while (cont != k):
	result += (pow(x,r)/factorial(r))*sinal
	r += 2
	sinal = -sinal
	cont += 1
	
print(round(result,6))