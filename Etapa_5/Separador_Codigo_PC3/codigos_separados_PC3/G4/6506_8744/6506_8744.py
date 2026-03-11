# faça seu código aqui!
a = int(input("digite um numero:" ))
b = input("s ou n: ")

R = 40

if (b == "s"):
	c = (a * R)
	d = c * 0.05
	e = c - d
	print(round(e,2))
else:
	e = a * R
	print(round(e,2))