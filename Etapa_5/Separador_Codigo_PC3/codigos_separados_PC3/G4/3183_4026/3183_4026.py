from numpy import*
v=array(eval(input("Vetor de numeros inteiros (decrescente):")))
m=size(v)
w=zeros(m, dtype=int)
for j in range(m):
	w[j]=v[- j-1]
print(w)