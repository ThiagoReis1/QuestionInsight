import math
pi = math.pi
x = eval(input(""))
k = int(input(""))
i = 0
indice = 2

while (x < k):
	x = 1-(x/indice)(math.factorial (k))
	i = i + 1
print(round(x, 6))