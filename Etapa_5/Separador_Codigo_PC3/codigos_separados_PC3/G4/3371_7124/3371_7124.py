u = input ("unidade (K ou M):")
v = float (input("valor da medida:"))

if (u.upper()) == "K":
	m= v/1.60934
	print (round (m,2))
else:
	k = 1.60934 * v
	print (round (k,2))