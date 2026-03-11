from numpy import*

v = array(eval(input("vetor: ")))

A = min(v)
B = max(v)

c = 0.75*A + 0.25*B
d = 0.25*A + 0.75*B

x = array(zeros(2, dtype = int ))
k = 0
g = 0
for i in range(size(v)):
	if v[i]>=A and v[i]<c:
		k = k + 1
		x[0]=k
	elif v[i]>=c and v[i]<d:
		g = g + 1
		x[1]=g
print(x)