gols = input("digite as gols retiradas:")
gols = gols.split(',')

contagem = [0, 0, 0, 0]
	
for gol in gols:
	if gol == 'A' :
		contagem[0] += 1
elif gol == 'B' :
	contagem[1] += 1
elif gol == 'C' :
	contagem[2] += 1
elif gol == 'D' :
	contagem[3] += 1
	
print('[{}]'.format(','.join(map(str, contagem)))