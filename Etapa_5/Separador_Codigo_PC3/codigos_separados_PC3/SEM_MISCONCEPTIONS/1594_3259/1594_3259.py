from numpy import *
dano = array(eval(input("Danos: ")))

k = 1
i = 0
total = 0

while(i<size(dano)):
	dano1 = dano[i] * k
	total = total + dano1
	k = k + 1
	i = i + 1

print (total)