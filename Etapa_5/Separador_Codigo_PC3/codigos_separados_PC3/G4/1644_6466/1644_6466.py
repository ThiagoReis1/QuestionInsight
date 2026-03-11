from numpy import*

notas = array(eval(input(": ")))

n = 0
for m in range(size(notas)):
	if notas[m] < 5:
		n = n + 1
		
i =zeros(n, dtype=int)
p = 0
for j in range(size(notas)):
	if notas[j] < 5:
		i[p] = j
		p = p + 1
		
print(n)
print(i)
		