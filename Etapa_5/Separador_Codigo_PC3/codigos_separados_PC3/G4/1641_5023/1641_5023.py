from numpy import*
v = array(eval(input("Quantidade de alunos: ")))
c = 0
for i in range(size(v)):
	if (v[i] % 3 == 0):
		c = c + 1
z = zeros(c,dtype=int)
c1 = 0
i = 0
for i in range(size(v)):
	if (v[i] % 3 == 0):
		z[c1] = i
		c1 = c1 + 1
print(c)
print(z)
		
	
