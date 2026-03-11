from numpy import*
cab = input('informe a cor do cabelo: ').upper().split(',')

cor = zeros(5, dtype=int)

for i in range(len(cab)):
	if cab[i] == 'P':
		cor[0] = cor[0] + 1
	elif cab[i] == 'C':
		cor[1] = cor[1] + 1
	elif cab[i] == 'R':
		cor[2] = cor[2] + 1
	elif cab[i] == 'L':
		cor[3] = cor[3] + 1
	elif cab[i] == 'B':
		cor[4] = cor[4] + 1
print(max(cor))
print(cor)
	