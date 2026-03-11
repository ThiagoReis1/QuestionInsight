from numpy import*

mens = array(eval(input("Codigo: ")))

for i in range(size(mens)):
	if mens[i] != 9:
		mens[i] = (mens[i] + 1)**3
	else:
		mens[i] = 0
print(mens)