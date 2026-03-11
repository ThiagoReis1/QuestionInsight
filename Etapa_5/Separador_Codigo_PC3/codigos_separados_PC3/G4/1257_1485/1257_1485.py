from numpy import*
v = array(eval(input("insira o vetor: ")))
a = min(v)
b = max(v)
c = 0.85*a + 0.15*b
d = 0.4*a + 0.6*b
x = zeros(2, dtype = int)
l = 0
k = 0
for i in range (size(v)):
	if ( v[i] >= a) and (v[i] < c):
		l = l + 1
		x[0] = l
	if (v[i] >= d) and (v[i] < b):
		k = k + 1
		x[1] = k
print (x)