from numpy import*
vet=array(eval(input("digite o vetor: ")))
A=min(vet)
B=max(vet)
C= 0.6 * A + 0.4 * B
D=0.3 * A + 0.7 * B
v=array([0,0])
for e in range(size(vet)):
	if(A <= vet[e] < C):
		v[0]=v[0]+1
	elif(C <= vet[e] < D):
		v[1]=v[1]+1
print(v)