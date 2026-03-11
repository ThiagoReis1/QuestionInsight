from numpy import*
a = array(eval(input("Quantidade de alunos por turma: ")))
c = 0
for i in range(size(a)):
	if (a[i]%2 == 0):
		c = c + 1
print(c)
v = zeros(c, dtype=int)
t = 0
for i in range(size(a)):
	if (a[i]%2 == 0):
		v[t] = i
		t = t + 1
print(v)
	

	