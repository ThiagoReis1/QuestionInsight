from numpy import*
osc = array(eval(input("ala: ")))
i = 1
x = 0
for i in range(1, size(osc)):
	if osc[i] >= osc[0]:
		print(i)
		x = x + 1
print(x)