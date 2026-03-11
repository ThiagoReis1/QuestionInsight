from numpy import*
f = array(eval(input("numero: ")))
z = zeros(size(f), dtype = int)
e = 0
for e in range (size(f)):
	if f[e]== 9:
		z[e]= 0
	else:
		z[e]=(f[e]+1)**2
		e=e+1
print(z)