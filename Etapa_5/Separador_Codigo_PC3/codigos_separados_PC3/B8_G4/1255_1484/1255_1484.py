from numpy import*
v = array(eval(input("insira o vetor:")))
a = min(v)
b = max(v)
c = 0.65 * a + 0.35 * b
d = 0.45 * a + 0.55 * b
x = zeros(2,dtype =int)
for i in range(size(v)):
	if ( v[i] >= a ) and ( v[i] < c ):
		x[0]= x[0] +1
	elif ( v[i] >= c ) and ( v[i]< d ):
		x[1] = x[1]+1
		
print(x)