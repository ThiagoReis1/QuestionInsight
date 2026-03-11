from numpy import*

x = array(eval(input("Digite: ")))
c = 0

for i in range(size(x)):
	if (x[i] >= 5.0):
		c += 1
print(c)

z = zeros(c, dtype=int)
j = 0

for i in range(size(x)):
	if (x[i] >= 5):
		z[j] = i
		j += 1
print(z)