# faça seu código aqui
from numpy import *
i = 0
u = 0
n = input().upper()
if "N" not in n:
	print("nao achei")
while i < len(n):
	if n[i] == "N":
		print(i)
	i+=1