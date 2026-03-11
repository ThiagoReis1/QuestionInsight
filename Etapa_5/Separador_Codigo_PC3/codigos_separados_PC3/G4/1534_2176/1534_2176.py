from math import *
x = float(input("Digite o número real: "))
k = int(input("Digite o termo: "))
arc = x
n = 1
m = 3
while(n<k):
	arc = arc + ((x**m)/m)
	m = m + 2
	n = n + 1	
print(round(arc, 7))
