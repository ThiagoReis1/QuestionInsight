# faça seu código aqui!
q = int(input("quantidade de combo "))
d = (15/100)

if q <= 3 :
	v = 20 * q 
	print(round(v,2))
else:
	v = (20*q)
	c = v - d*v
	print(round(c,2))