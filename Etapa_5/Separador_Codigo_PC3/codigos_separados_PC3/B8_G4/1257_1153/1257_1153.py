from numpy import*
vet= array(eval(input("digite o vetor")))
a=min(vet)
b=max(vet)
c=0.85 * a + 0.15 * b
d=0.4 * a + 0.6 * b
v=array([0,0])
for ind in range(size(vet)):
	if(a<= vet[ind] < c):
		v[0] = v[0] + 1
	elif(d<= vet[ind] <b):
		v[1]= v[1] +1
print(v)