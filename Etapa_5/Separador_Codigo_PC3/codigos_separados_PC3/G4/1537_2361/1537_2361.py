from math import *
x = float(input("Um Num. Real: "))
k = int(input("Quantidade de termos da Série: "))
i = 1
es = 1
while (k > 0) and (i < k):
	es = es + ((x**(i)) / factorial(i))
	i = i + 1

print (round(es, 9))
