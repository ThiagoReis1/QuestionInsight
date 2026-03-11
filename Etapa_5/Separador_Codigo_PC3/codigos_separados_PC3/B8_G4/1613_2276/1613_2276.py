from numpy import *
atv = array(input())
t = array(eval(input()))

k = zeros(size(atv))

y = 0
while y < size(atv):
	if atv[y] == "ALONGAMENTO":
		k[x] = t[y]*3
		x = x + 1
	elif atv[y] == "CORRIDA":
		k[x] = t[y]*10.3
		x = x + 1
	elif atv[y] == "DANCA":
		k[x] = t[y]*6.7
		x = x + 1
	elif atv[y] == "ESCALADA":
		k[x] =t[y]*9.7
		x = x + 1
	elif atv[y] == "HIDROGINASTICA":
		k[x] == t[y]*5
		x = x + 1
	y = y + 1
		
print(round(sum(k), 2))