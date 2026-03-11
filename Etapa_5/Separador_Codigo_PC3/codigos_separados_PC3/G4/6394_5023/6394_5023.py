from numpy import*
v = array(eval(input("Vetor: ")))
c = zeros(size(v),dtype=int)
for i in range(size(v)):
	if (v[i] == 9):
		c[i] = 0
	else:
		c[i] = v[i] + 1
print(c)