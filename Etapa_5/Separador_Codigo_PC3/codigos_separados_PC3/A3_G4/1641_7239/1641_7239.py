from numpy import*
t = array(eval(input("Numero de pessoas na turma: ")))
c1 = 0
c2 = 0
for i in range(size(t)):
	if t[i] % 3 == 0:
		c1 = c1 + 1
print(c1)
z = zeros(c1, dtype=int)
j=0
for i in range(size(t)):
	if t[i] % 3 == 0:
		z[j] = i
		j = j + 1
print(z)