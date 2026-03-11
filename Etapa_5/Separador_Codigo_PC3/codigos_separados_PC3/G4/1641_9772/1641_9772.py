from numpy import*
turmas= array (eval(input('')))
trio = 0
for i in range(size(turmas)):
	if turmas [i] % 3 == 0:
		trio += 1
ind= zeros(trio, dtype=int)
print(trio)
j=0
for i in range(size(turmas)):
	if turmas [i] % 3 == 0:
		ind [j] = i 
		j += 1
print(ind)