# faça seu código aqui!
from numpy import *

v = input("Digite: ").upper()

i = 0

while i < len(v):
	if v[i] == 'L':
		print(i)
	i = i + 1
if 'L' not in v:
	print("nao achei")