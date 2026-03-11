from numpy import *
v = array(eval(input("digite: ")))
p = input("digite: ").upper()
i = 0
j = 0
pos = 0
while (i < len(v)):
	d = p.replace("R","L")
	if (v[i] == d):
		pos = i
		v[i] = v[i] + p
		j = 1
		print(pos)
	i = i + 1

if (j == 0):
	print("NAO ENCONTRADA")

