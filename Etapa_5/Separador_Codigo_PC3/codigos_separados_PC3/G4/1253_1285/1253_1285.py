from numpy import*
v = array(eval(input("digite o vetor: ")))
a = min(v);
b = max(v);
c = 0.6 * a + 0.4*b
d = 0.3 * a + 0.7*b
x1=0
x2=0
x = ones(2,dtype=int)
for i in range (size(v)):
	if (v[i]>=a and v[i]<c):
		x1 = x1+1
	if (v[i]>=d and v[i]<b):
		x2 = x2+1
x[0] = x1
x[1] = x2
print (x)