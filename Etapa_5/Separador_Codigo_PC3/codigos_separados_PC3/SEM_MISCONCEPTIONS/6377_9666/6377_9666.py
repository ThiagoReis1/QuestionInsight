from numpy import *

entrada = input().split(',')

player = ['A', 'B', 'C', 'D']
qtd_gol = [0, 0, 0, 0]

for i in entrada:
	for n in range(4):
		if i == player[n]:
			qtd_gol[n] += 1
			
print(array(qtd_gol))