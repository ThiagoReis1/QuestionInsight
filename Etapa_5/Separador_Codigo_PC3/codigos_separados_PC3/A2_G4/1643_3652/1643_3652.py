from numpy import *
n = array(eval(input("notas finais: ")))
i = 0
for x in range(size(n)):
	if (n[x] >= 5) :
		i = i + 1
	else:
		i = i
print(i)
z = zeros(i, dtype = int)
q = 0
for w in range(size(n)):
	if (n[w] >= 5):
		z[q] = z[q] + w
		q = q + 1
print(z)