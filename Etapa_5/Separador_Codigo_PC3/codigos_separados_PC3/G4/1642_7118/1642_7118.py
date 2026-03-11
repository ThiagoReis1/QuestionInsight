from numpy import*

turma = array(eval(input()))
acum = 0

for i in range(size(turma)):
	if turma[i] % 5 == 0:
		acum = acum + 1
		
a = zeros(acum, dtype = int)
b = 0
		
for i in range(size(turma)):
	if turma[i] % 5 == 0:
		a[b] = i
		b = b + 1

print(acum)
print(a)

