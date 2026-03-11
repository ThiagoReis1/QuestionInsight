from numpy import*
r=0
k=[]
v = array(eval(input(" vetor: ")))

for i in range(size(v)):
	if (v[i] < 70):
		r=r+1
		k.append(i)

l=zeros(size(k), dtype(int))
l=l+k
print(r)
print(l)
