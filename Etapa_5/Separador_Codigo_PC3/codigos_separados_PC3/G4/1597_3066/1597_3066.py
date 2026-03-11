from numpy import *
vc = array(eval(input("digite: ")))
i = 0
ct = 0
while (i < size(vc)):
	if (vc[i] > 80):
		vc[i] = vc[i] - 5
	ct = vc[i] + ct
	i = i + 1
print(round(ct, 2))
	