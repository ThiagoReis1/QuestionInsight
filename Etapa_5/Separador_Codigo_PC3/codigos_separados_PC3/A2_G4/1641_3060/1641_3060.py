from numpy import *
v = array(eval(input("Turmas: ")))
trio = 0

for i in range(size(v)):
	if (v[i] % 3 == 0):
		trio = trio + 1
print(trio)
vs = zeros(trio, dtype = int)
j = 0
for i in range(size(v)):
	if (v[i] % 3 == 0):
		vs[j] = vs[j] + i
		j = j + 1
	else:
		j = j
print(vs)