from numpy import*
v=array(eval(input("digite vetor:")))
A = min(v)
B = max(v)
C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B
cont=zeros(2,dtype=int)
for i in range(size(v)):
	if D>v[i] and C<=v[i]:
		cont[0] = cont[0]+1
	elif D<=v[i] and B>v[i]:
		cont[1] = cont[1]+1
print(cont)		
