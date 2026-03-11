x  = input("K ou M?")
v = float(input("velocidade?"))
z = (v*3.6)
w = (v/3.6)
if(x.upper() == "K"):
	print(round(w, 2))
else:
	print(round(z, 2))

	