from numpy import*
turmas = array(eval(input(':')))

t = 0
for i in range(size(turmas)):
	if turmas[i] % 5 == 0:
		t = t + 1
e = 3
s = 0
it = zeros(t, dtype=int)
for x in range(size(turmas)):
	e = e + 1
	s = s + 1
	if turmas[i] % 5 == 0:
		it[0] = it[0] + 1
		s = s + 1
		
print(t)
print(it)