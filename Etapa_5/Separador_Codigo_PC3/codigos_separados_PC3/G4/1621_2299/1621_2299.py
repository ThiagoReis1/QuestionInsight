from numpy import*

v = array(eval(input("")))
v2 = array(eval(input("")))

f = 0
i = 1
k = 0

while (size(v) >= i):
	i = i + 1
	if (v[k] == "ARROZ"):
		f = f + (1.25 * v2[k])
	elif (v[k] == "FEIJAO"):
		f = f + (2.6 * v2[k])
	elif (v[k] == "BIS"):
		f = f + (1.8 * v2[k])
	elif (v[k] == "MIOJO"):
		f = f + (0.85 * v2[k])
	else:
		f = f + (3.2 * v2[k])
	k = k + 1
	

print(f)

	


	