from numpy import*

x = array(eval(input("numero de alunos")))
m = 0
j = 0
for i in range(size(x)):
	if (x[i] % 3 == 0):
		m = m + 1
print(m)

p = zeros(m, dtype=int)

for i in range(size(x)):
	if (x[i] % 3 == 0):
		p[j] = i
		j = j + 1
		
print(p)
	