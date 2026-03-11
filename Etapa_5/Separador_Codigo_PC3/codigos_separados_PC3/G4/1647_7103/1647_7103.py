from numpy import*
f = array(eval(input("Frequencia: ")))
a = 0
for i in range(size(f)):
	if f[i] >= 70:
		a = a + 1
print(a)
b = zeros(a,dtype=int)
c = 0
for i in range(size(f)):
	if f[i] >= 70:
		b[c] = i
		c = c + 1
print(b)