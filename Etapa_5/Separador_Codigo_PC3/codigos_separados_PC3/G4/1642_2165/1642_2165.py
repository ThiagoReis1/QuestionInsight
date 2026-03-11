from numpy import*
vetTurma = array(eval(input()))

soma = 0
for x in range(size(vetTurma)):	
	if(vetTurma[x] % 5 == 0):
		soma = soma + 1
print(soma)


v = zeros(soma, dtype=int)	
acum = 0

for z in range(size(vetTurma)):
	if(vetTurma[z] % 5 == 0):
		v[acum] = z
		acum = acum + 1
print(v)
		