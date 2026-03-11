from numpy import*
vet = array(eval(input("Informe o vetor")))
A = min(vet)
B = max(vet)
C = 0.75*A + 0.25*B
D = 0.25*A + 0.75*B
x = array([0,0])
i = size(vet)
for ind in range(i):
	if(A <= vet[ind] < C):
		x[0] = x[0] + 1
	elif(D <= vet[ind] < B):
		x[1] = x[1] + 1
print(x)