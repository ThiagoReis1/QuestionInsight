from numpy import *
v = input("string: ").split(",")

vetor = zeros(5, dtype=int)

P = 0
C = 0
R = 0
L = 0
B = 0

for i in range(size(v)):
	if(v[i] == 'P'):
		P = P + 1
	elif(v[i] == 'C'):
		C = C + 1
	elif(v[i] == 'R'):
		R = R + 1
	elif(v[i] == 'L'):
		L = L + 1
	elif(v[i] == 'B'):
		B = B + 1

		
vetor[0] = P 
vetor[1] = C
vetor[2] = R
vetor[3] = L
vetor[4] = B
print(max(vetor))
print(vetor)