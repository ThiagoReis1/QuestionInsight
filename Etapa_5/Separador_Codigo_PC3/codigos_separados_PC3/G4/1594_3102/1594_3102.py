from numpy import*
v = array(eval(input("vetor de danos:")))
i = 0
p = 1

dano = 0

while(i<size(v)):
	dano = dano + v[i] * p
	p = p + 1
	i = i + 1

print(dano)