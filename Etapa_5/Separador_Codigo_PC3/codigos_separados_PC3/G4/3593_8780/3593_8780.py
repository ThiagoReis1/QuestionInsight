from numpy import *
v = array(eval(input("Digite os valores do dado: ")))
i = 0
p = 200

while i < size(v):
	if v[i] == 1 or v[i] == 3 or v[i] == 5:
		p = p / 2
	else:
		p = p * 3
	i += 1

print(round(p, 2))
		
	