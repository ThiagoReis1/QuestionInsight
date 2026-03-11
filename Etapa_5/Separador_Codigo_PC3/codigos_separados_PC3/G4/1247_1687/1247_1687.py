from numpy import*
v = array(eval(input("Digite o valor do vetor: ")))
x = zeros(2, dtype = int)

c = 0.75 * min(v) + 0.25 * max(v)
d = 0.25 * min(v) + 0.75 * max(v)
for i in range(0, size(v)):
	if (v[i]>=min(v) and v[i] < c):
		x[0] = x[0] + 1
	if (v[i] >= d and v[i] < max(v)):
		x[1] = x[1] + 1
print(x)