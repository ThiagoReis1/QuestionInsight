from numpy import *

X = array(eval(input("Vetor de entrada: ")))

A = [1, 2, 3, 4]
B = [80, 40, 20, 10]

i = 0
j = 0
TP = 0

while j < size(X):
	if X[j] != A[i]:
		i += 1
	else:
		TP += B[i]
		i = 0
		j += 1

print(TP)
		