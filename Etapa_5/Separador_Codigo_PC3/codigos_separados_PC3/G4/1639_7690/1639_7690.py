from numpy import*
a = array(eval(input("Vetor:")))
b = zeros(size(a),dtype = int)
par = 0
for i in range(size(a)):
	if (a[i] % 2 == 0):
		b[par] = i
		par = par + 1

print(par)
print(b[0:par])
