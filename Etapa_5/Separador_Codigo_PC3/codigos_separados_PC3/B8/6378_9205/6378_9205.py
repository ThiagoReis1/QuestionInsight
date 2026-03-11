from numpy import*
notas = input().upper().split(',')
qtds = zeros(4, dtype = int)
for i in range(size(notas)):
	n = notas[i]
	if n == 'U':
		qtds[3] +=1
	elif n == 'V':
		qtds[2] += 1
	elif n == 'D':
		qtds[1] += 1
	elif n == 'C':
		qtds[0] += 1
		
print(qtds)


