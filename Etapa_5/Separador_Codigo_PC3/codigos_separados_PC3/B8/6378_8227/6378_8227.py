notas = input("digite as notas retiradas: ")
notas = notas.split(',')

contador = [0, 0, 0, 0]

for nota in notas:
	if nota == 'C':
		contador[0] += 1
	elif nota == 'D':
		contador[1] += 1
	elif nota == 'V':
		contador[2] += 1
	elif nota == 'U':
		contador[3] += 1
		

print('[{}]'.format(' '.join(map(str, contador))))
