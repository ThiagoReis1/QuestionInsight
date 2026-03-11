from numpy import*

v = array(eval(input()))

p = 100
i = 0


while i < size(v):
	if v[i] == 1:
		p = p * 5
	elif v[i] == 2:
		p = p * 3
	elif v[i] == 4:
		p = p / 2
	i = i + 1

print(p)