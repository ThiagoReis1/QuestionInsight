from numpy import* 
A = input().upper().split(",")
aux = zeros (4, dtype = int)
for i in range(0, size(A)):
	if A[i] == "A":
		aux[0] += 1
	elif A[i] == "B":
		aux[1] += 1
	elif A[i] == "L":
		aux[2] += 1
	elif A[i] == "H":
		aux[3] += 1
print(aux)
