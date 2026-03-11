from numpy import *

v = array(eval(input("v: ")))
n = int(input("Digite o numero inteiro n: "))
i = 0
a = 0

while i < size(v):
	if (v[i] == n):
		print(i)
	elif (v[i] > n):
		a = a + 1
	i = i + 1
print(a)