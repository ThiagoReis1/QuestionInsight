from numpy import *
v = input("Digite: ").upper()
i = 0
c = 0
t = len(v)
while i < t:
	if v[i] == "M":
		print(i)
		c = c + 1
	i = i + 1
if c == 0:
	print("nao achei")
	
	