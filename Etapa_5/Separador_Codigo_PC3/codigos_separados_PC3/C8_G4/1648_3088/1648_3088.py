from numpy import*
v = array(eval(input("Insira o vetor: ")))
r = 0
for i in range(size(v)):
	if v[i]<70:
		r = r + 1
	i = i + 1
v0 = zeros(r, dtype=int)
i = 0
c = 0
for i in range(size(v)):
	if v[i]<70:
		v0[c] = i
		c = c + 1
print(r)
print(v0)
	
	