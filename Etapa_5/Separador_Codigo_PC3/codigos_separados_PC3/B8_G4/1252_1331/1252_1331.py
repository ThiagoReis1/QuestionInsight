from numpy import*
vetor = array(eval(input("Insira o vetor: ")))
x = zeros(2,dtype=int)
A = min(vetor)
B = max(vetor)
C = 0.6*A + 0.4*B
D = 0.3*A + 0.7*B
for i in vetor:
	if (i>=A) and (i<C):
		x[0] += 1
	elif(i>=C)and(i<D):
		x[1] += 1
print (x)