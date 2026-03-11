entrada = input()

entrada = entrada.split(',')
saida = [0,0,0,0]

for i in entrada:
	if(i == 'C'):
		saida[0] += 1
	elif (i == 'D'):
		saida[1] += 1
	elif (i == 'V'):
		saida[2] += 1
	elif (i == 'U'):
		saida[3] += 1

print('[',end='')
for i in range(4):
	if(i == 3):
		print(saida[i],end=']')
	else:
		print(saida[i],end=' ')
	
