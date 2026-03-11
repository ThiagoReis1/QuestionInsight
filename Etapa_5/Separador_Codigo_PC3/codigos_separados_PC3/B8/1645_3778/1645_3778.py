from numpy import*

saques = array(eval(input()))
n = 0
cont = 0
for i in range(0, len(saques), 1):
	if saques[i] >= 2000 and cont == 0:
		indices = [i]
		cont = 1
		n = n + 1
	elif saques[i] >= 2000 and cont != 0:
		indices = indices + [i]
		n = n + 1
print(n)
resp = zeros(len(indices), dtype=int)
for i in range(0, len(indices), 1):
	resp[i] = indices[i]
print(resp)