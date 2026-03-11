from numpy import*

v = array(eval(input("")))
dano = 0

for i in range(0, size(v)):
	dano = dano + (i + 1)*v[i]
	
print(dano)