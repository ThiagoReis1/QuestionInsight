from numpy import*
v = array(eval(input("Digite as notas: ")))
a = 0
for n in range(size(v)):
	if (v[n]>=5):
		a = a + 1
print(a)
v2 = zeros(a, dtype=int)
x = 0
for i in range(size(v)):
	if (v[i]>=5):
		v2[x] = i
		x = x + 1
print(v2)

