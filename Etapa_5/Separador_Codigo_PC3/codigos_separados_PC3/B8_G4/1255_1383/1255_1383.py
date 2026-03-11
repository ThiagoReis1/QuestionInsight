from numpy import*
vetor=array(eval(input("")))
A=min(vetor)
B=max(vetor)
C= 0.65 * A + 0.35 * B
D= 0.45 * A + 0.55 * B
v=zeros(2,dtype=int)
for i in vetor:
	if(i>=A and i<C):
		v[0]+=1
	elif(i>=C and i<D):
		v[1]+=1
print(v)		