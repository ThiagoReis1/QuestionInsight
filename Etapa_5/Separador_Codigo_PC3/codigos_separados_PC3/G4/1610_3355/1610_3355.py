from numpy import *
a = input("string contendo numeros inteiros no formato CSV: ")

v = a.split(',')

n = 0
while (n < size(v)):
	v[n] = int(v[n])
	n = n + 1
print(sum(v))
