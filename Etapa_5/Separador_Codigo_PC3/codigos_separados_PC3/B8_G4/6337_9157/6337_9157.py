from numpy import *
v = array(eval(input()))
N = int(input())
cont = 0

for i in range(size(v)):
	if N == (v[i]):
		print(i)
	elif 	v[i] < N:
		cont = cont + 1
print(cont)
		
		

		