from numpy import*
v = array(eval(input("Porc de aulas frequentadas: ")))
q = 0
for i in range(size(v)):
	if (v[i]>=70):
		q = q + 1
print(q)

z = zeros(q, dtype = int)
x = 0
for j in range(size(v)):
	if (v[j]>=70):
		z[x] = j
		x = x + 1
print(z)