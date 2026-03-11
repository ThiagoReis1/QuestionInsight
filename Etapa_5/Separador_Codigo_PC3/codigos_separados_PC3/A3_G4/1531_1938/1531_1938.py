from math import*
angulo = eval(input(""))
k = int(input(""))
fact = 2
ind = 2
x = 1
i = 1
sinal = -1
while(i != k):
	if(i%2 == 0):
		sinal = 1
	else:
		sinal = -1
	angulo = x + sinal * (angulo ** ind/factorial(2 + fact))	
	ind = ind + 2
	fact = fact + 2
	i = i + 1
print(x)