from numpy import*
vetor=array(eval(input("")))
a=min(vetor)
b=max(vetor)
c=0.75*a + 0.25*b
d=0.25*a + 0.75*b
v=zeros(2,dtype=int)
for i in vetor:
		if(i>=a and i<c):
			v[0]+=1
		elif(i<=d and i<b):
			v[1]+=1
print(v)