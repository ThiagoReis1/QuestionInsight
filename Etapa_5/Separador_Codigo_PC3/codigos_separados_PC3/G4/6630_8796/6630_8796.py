# faça seu código aqui!
from numpy import *

pos = input().upper()

i = 0

while i < len(pos):
	if pos[i] == 'L':
		print(i)
	i += 1
	
if 'L' not in pos:
	print('nao achei')