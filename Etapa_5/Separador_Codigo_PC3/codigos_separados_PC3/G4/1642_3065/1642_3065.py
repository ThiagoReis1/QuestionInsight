from numpy import*
vet = array(eval(input("vetor de turmas: ")))

v = zeros(3,dtype=int)

s=0

for i in range(size(vet)):
	if(vet[i]%2==0):
		s=s+1
print(s-1)

j=0

for i in range(size(v)):
	if(v[i]%2==0):
		j=j+1
		
print(v)	