from numpy import*
v = array(eval(input("lista de alunos: ")))
a = 0
for i in range(len(v)):
	if (v[i] % 5 == 0):
		a = a + 1
c = zeros(size(a),dtype = int)
n = 0
for j in range(len(v)):
	if (v[j] % 5 == 0):
		c[n] = j
		n = n + 1
print(a)
print(c)