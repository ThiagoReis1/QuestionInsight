from numpy import*

v = array(eval(input("V: ")))

saida = ""

i = 0
g = size(v)-1
if size(v) > 1:
	while i < size(v)-2:
			saida = saida + str(v[i]) + "x" + "^" + str(g) + " + "
			i += 1
			g -= 1

	saida = saida + str(v[i]) + "x" + " + " + str(v[i+1])
	print(saida)
else:
	print(v[0])