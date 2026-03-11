from numpy import *
v = array(eval(input("vetor de numeros: ")))
p = 200
i = 0
while i < size(v):
	if v[i] == 1:
		p = p / 2
	if v[i] == 2:
		p = p * 3
	if v[i] == 3:
		p = p / 2
	if v[i] == 4:
		p = p * 3
	if v[i] == 5:
		p = p / 2
	if v[i] == 6:
		p = p * 3
	i = i + 1
print(round(p, 2))
	