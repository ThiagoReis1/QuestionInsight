import math
x = float(input(""))
k = int(input(""))
i = 0
indice = 0
cos = 0
while(i<k):
	cos = cos + (x**indice)/math.factorial(indice)
	i = i + 1
	indice = indice + 2
print(round(cos,8))
	
