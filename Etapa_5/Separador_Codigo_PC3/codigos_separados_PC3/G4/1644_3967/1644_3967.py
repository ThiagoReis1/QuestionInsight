from numpy import*

n = array(eval(input()))
r = 0

#descobrir como transforma string em vetor

for i in n:
	if i < 5:
		r = r + 1

aux = zeros(r, dtype=int)
j = 0

for i in range(size(n)):
	if n[i] < 5:
		aux[j] = i
		j = j + 1

print(r)
print(aux)