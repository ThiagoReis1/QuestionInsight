import math
x = float(input(""))
k = int(input(""))
i = 0
indice = 1
seno = 0
while(i<k):
	seno = seno + (x**indice)/math.factorial(indice)
	i = i + 1
	indice = indice+2
print(round(seno,9))

