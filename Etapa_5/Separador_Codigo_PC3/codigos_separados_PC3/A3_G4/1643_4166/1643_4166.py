from numpy import*
notas=array(eval(input("Vetor de notas:")))
n=size(notas)
soma=0
v=zeros(n, dtype=int)

for i in range(n):
	if(notas[i]>=5):
		v[i]=notas[i]
		print()
		x=size(notas)
print(v)
