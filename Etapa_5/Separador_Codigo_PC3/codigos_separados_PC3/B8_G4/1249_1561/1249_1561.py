from numpy import*
v = array(eval(input("Informe o vetor: ")))
x = zeros(2, dtype = int)
c = 0.7 * min(v) + 0.3 * max(v)
d = 0.4 * min(v) + 0.6 * max(v)
for i in range (0, size(v)):
	if (v[i] >= min(v) and v[i] < c):
		x[0] = x[0]	+ 1
	elif (v[i] >= c and v[i] < d):
		x[1]= x[1] + 1
print(x)