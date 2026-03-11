# faça seu código aqui!
from numpy import*

n = input().upper()
t = 0
i = 0

while i < len(n):
	if n[i] == "P":
		print(i)
		t = t + 1
	i = i + 1
if t == 0:
	print("nao achei")
	

	