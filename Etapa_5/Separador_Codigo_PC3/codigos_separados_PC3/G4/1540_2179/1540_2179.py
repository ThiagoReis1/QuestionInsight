from math import *

x = eval(input("ângulo: "))
k = float(input("Quantidade de termo: "))
i = 1
coss = 1

while(x>0) and (k>i):
	coss = coss + (x**(i)/factorial(i*2)) * (-1)**(i)
	i = i + 1
print(round(coss, 6))