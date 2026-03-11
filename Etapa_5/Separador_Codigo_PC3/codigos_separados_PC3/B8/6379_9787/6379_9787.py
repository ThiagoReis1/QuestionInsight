from numpy import*

notas = input("").upper().split(',')
contador = zeros(5, dtype=int)

for i in notas:
	if i == 'A':
		contador[0] += 1
	elif i == 'B':
		contador[1] += 1
	elif i == 'C':
		contador[2] += 1
	elif i == 'D':
		contador[3] += 1
	elif i == 'E':
		contador[4] += 1
		
print(contador)