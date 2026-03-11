from numpy import *
dano = array(eval(input("danos: ")))
i = 0
total = 0
while (i < size(dano)):
	total = total + dano[i] * (i + 1)
	i = i + 1
print(total)
	